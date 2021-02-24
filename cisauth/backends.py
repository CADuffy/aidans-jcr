"""
This is the CIS Authentication.
This might need to be changed if a more secure method of auth is available
(e.g. Shibboleth).
"""
from django.contrib.auth.models import User
import requests
import time


class CISBackend(object):
    def authenticate(self,request,username=None,password=None):
        """Authenticate with the Durham backend, to check username and password"""
        # TODO: ideally check they are a member of Aidan's. In practice, this is more challenging.
        # Not if you let others do the heavy lifting :)

        # see if the user is valid on the Durham server
        validator_resp = requests.get('https://www.dur.ac.uk/its/password/validator', auth=(username,password))

        # Make name case insensitive, as we don't want to create two users by accident
        username_case_insensitive = username.lower()

        if(validator_resp.status_code != 401):
            try:
                return User.objects.get(username=username_case_insensitive)
            except User.DoesNotExist:
                # Check if the user is an Aidans student
                user_data = requests.get('https://community.dur.ac.uk/grey.jcr/itsuserdetailsjson.php?username=' + username_case_insensitive)
                user_college = user_data.json().college

                if user_college == "St Aidan's College":
                    # Create a new Django user, getting information from the info database
                    user = User(username=username_case_insensitive)
                    user.is_staff = False
                    user.is_superuser = False
                    user.email = username_case_insensitive + "@durham.ac.uk"
                    user.save()
                    return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
