from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

##################TODO:######################
# from .models import Profile, Post
# Profile MODEL
# Post MODEL
#############################################



class ExampleTest(TestCase):
    
    def setUp(self):
        # Setup code can go here if needed
        self.value1 = 1
        self.value2 = 2
        self.value3 = None
        self.container = [1, 2, 3]

    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertFalse(self):
        self.assertFalse(False)

    def test_assertEqual(self):
        self.assertEqual(self.value1, 1)

    def test_assertNotEqual(self):
        self.assertNotEqual(self.value1, self.value2)

    def test_assertIsNone(self):
        self.assertIsNone(self.value3)

    def test_assertIsNotNone(self):
        self.assertIsNotNone(self.value1)

    def test_assertIn(self):
        self.assertIn(1, self.container)

    def test_assertNotIn(self):
        self.assertNotIn(4, self.container)

    def test_assertRaises(self):
        with self.assertRaises(ValueError):
            raise ValueError("This is a ValueError!")

    def test_assertIs(self):
        self.assertIs(True, True)

    def test_assertIsNot(self):
        self.assertIsNot(True, False)

    def test_assertContains(self):
        response = self.client.get(reverse('auth:signup'))
        self.assertContains(response, 'Sign Up')  

    def test_assertNotContains(self):
        response = self.client.get(reverse('auth:signup'))
        self.assertNotContains(response, 'Something that will definitely not be on this page')

    def test_assertRedirects(self):
        response = self.client.get(reverse('auth:userprofile'))
        self.assertRedirects(response, reverse('auth:signin'))

    def test_assertTemplateUsed(self):
        response = self.client.get(reverse('auth:signin'))
        self.assertTemplateUsed(response, 'signin.html')  

    def test_assertInHTML(self):
        response = self.client.get(reverse('auth:signin'))
        self.assertInHTML('<p>Sign in</p>', response.content.decode())

    def test_assertNotInHTML(self):
        response = self.client.get(reverse('auth:signin'))
        self.assertNotIn('Something that will definitely not be on this page', response.content.decode())




class PageExistsTest(TestCase):
    
    def test_something(self):
        self.assertEqual(1, 1)
        
    def test_admin_page_exists(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)
        
    def test_honeypot_page_exists(self):
        response = self.client.get(reverse('admin_honeypot'))
        self.assertEqual(response.status_code, 200)
        
    def test_404_page_exists(self):
        response = self.client.get('non/existent/page')
        self.assertEqual(response.status_code, 404)



       
class AuthTest(TestCase):
    
    def test_sign_up_user(self):
        
        user_data = {
            'email': 'test@email.com',
            'username': 'test',
            'password1': 'test',
            'password2': 'test'            
        }
        
        response = self.client.post(reverse('auth:signup'), user_data, format='text/html')
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('auth:userprofile'), args=[user_data['username']])
        self.assertEqual(response.status_code, 200)
        
   

class SignUpSetUp(TestCase):
    
    def setUp(self):
        user_data = {
            'email': 'test@email.com',
            'username': 'testuser',
            'password1': 'testpass',
            'password2': 'testpass'            
        }
        self.client.post(reverse('auth:signup'), user_data, format='text/html')


class SignInSetUp(TestCase):
    
    login_success = False
    
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'
        self.login_success = self.client.login(username=self.username, password=self.password)
    
    
   
    
        
class ProfileEditTest(SignInSetUp):
    
    def test_sign_in_success(self):
        self.assertTrue(self.login_success)
    
    def test_profile_edit_login_redirect(self):
        self.client.logout()
        response = self.client.get(reverse('auth:profile_edit'))
        self.assertEqual(response.status_code, 302)
    
    def test_profile_edit(self):
        response = self.client.get(reverse('auth:profile_edit'))
        self.assertEqual(response.status_code, 200)


class UserTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.get(username='testuser')

    def test_user_exists(self):
        self.assertTrue(self.user)

    def test_user_email_address(self):
        self.assertTrue(self.user.email, 'test@email.com')

    # def test_user_profile(self):
    #     profile = Profile.objects.get(user=self.user)
    #     self.assertTrue(self.user.profile)

    def test_post_create(self):
        response = self.client.get(reverse('post:create'))
        self.assertEqual(response.status_code, 200)
        
        form_data = {
            'title': 'Test Title',
            'content': 'Test Content'
        }
        response = self.client.post(reverse('post:create'), form_data, format='text/html')
        self.assertEqual(response.status_code, 302)
        
        self.assertTrue(Post.objects.filter(title='Test Title', content='Test Content').exists())
        
        
        blog_page = self.client.get(reverse('blog:index'))
        self.assertContains(blog_page, 'Test Title')
        
        post = Post.objects.filter(title='Test Title', content='Test Content')
        post.delete()
        self.assertNotContains(blog_page, 'Test Title')
        
        
        
        
        