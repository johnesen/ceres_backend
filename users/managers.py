from django.contrib.auth.models import BaseUserManager as BUM
# from djongo.models import Manager

class BaseUserManager(BUM):
    use_in_migrations = True

    def _create_user(self, email, is_superuser, is_active, password=None):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email=self.normalize_email(email=email),
            is_superuser=is_superuser,
            is_active=is_active,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None):
        """
        create user
        """
        return self._create_user(email=email, is_superuser=False, is_active=True, password=password)

    def create_superuser(self, email, password=None):
        """
        superuser creation
        """
        return self._create_user(email=email, is_superuser=True, is_active=True, password=password)
