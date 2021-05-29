from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your tests here.
class TestProfileClass(TestCase):
    """
    Test class that holds profile test cases
    """

    # Set up method
    def setUp(self) -> None:
        self.new_user = User(username='root', password='root', email='root@root.com')
        self.new_user.save()

        self.new_profile = Profile(user=self.new_user, profile_picture='default.png')

    # Teardown method
    def tearDown(self) -> None:
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, profile_picture='default.png')
        self.new_profile.save()

        self.new_user.delete()
        self.new_profile.delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    # Test save profile
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) > 0)

    # Test save multiple profiles
    def test_save_multiple_profiles(self):
        self.test_user = User(username='test', password='123', email='root@root.com')
        self.test_user.save()

        test_profile = Profile(user=self.test_user, profile_picture='default.png')

        self.new_profile.save_profile()
        test_profile.save_profile()

        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 1)

    # Test delete profile
    def test_delete_profile(self):
        self.new_profile.save_profile()

        self.new_profile.delete_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) < 1)

    # Test find user by username
    # def test_find_user_by_username(self):
    #     self.new_profile.save_profile()
    #
    #     test_user = User(username='test', password='123', email='root@root.com')
    #     test_user.save()
    #
    #     test_profile = Profile(user=test_user, profile_picture='default.png')
    #     test_profile.save_profile()
    #
    #     found_user = Profile.find_by_username("test")
    #     self.assertEqual(found_user.user.email, test_profile.user.email)
