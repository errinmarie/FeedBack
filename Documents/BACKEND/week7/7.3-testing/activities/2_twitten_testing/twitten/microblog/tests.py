from django.test import TestCase

from django.contrib.auth.models import User
from .models import Tweet


class CreatingNewUserTestCase(TestCase):
    def test_shows_homepage_text(self):
        # Quick check to make sure the text "Yell about" exists on the
        # homepage, since it should no matter what
        response = self.client.get('/')
        self.assertContains(response, 'Yell about')

    def test_homepage_shows_all_tweets_link(self):
        # TODO:
        # Make sure there is the text "All Tweets" in the homepage, to ensure
        # the all tweets link is there. See the previous test as an example.
        # Bonus: Also check for "all-tweets/" to ensure the link is correctly
        # rendered.
        
        response = self.client.get('/')
        self.assertContains(response, 'All Tweets')
        
        pass

    def test_shows_form(self):
        # Let's make sure that the homepage shows the expected form. To do so,
        # we just "spot check" for a few different expected bits of text.
        response = self.client.get('/')
        self.assertContains(response, 'Username:')
        self.assertContains(response, 'First name:')
        self.assertContains(response, 'Last name:')
        html = '<input type="text" name="username"'
        self.assertContains(response, html)

    def test_submit_creates_new_user(self):
        # First make sure we don't have any users
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)

        # Now we simulate the post request generated by
        # the form
        self.client.post('/', {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpass',
            'email': 'testuser@fake.com',
        })

        # Then, we check that a new user was created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # ...and we check that the user has the
        # properties we entered into the form
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'testuser@fake.com')



class TweetListsAppearTestCase(TestCase):
    # TODO Challenge 5 -- Create a setUp method to DRY
    # out your test

    def test_all_tweets_page_shows_a_tweet(self):
        fake_user = User.objects.create(username='test')
        Tweet.objects.create(
            user=fake_user,
            text="This is a testing tweet",
        )

        response = self.client.get('/all-tweets/')

        # TODO Challenge 3 -- use "self.assertContains" to check that
        # the tweet appears on the page.


    # TODO Challenge 4 -- Make a new test within this "TestCase" that
    # checks that the tweet also shows up on the user page





# TODO Challenge 7 -- Test create tweet form






