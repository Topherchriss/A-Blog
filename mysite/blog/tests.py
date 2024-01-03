from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User

class PostListViewTests(TestCase):
    def test_post_list_view_with_no_posts(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_post_list_view_with_posts(self):
        # Create test data
        author = User.objects.create_user(username='testuser', password='testpassword')
        Post.objects.create(title='Test Post', text='Test Content', author=author, published_date=timezone.now())

        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['posts'], ['<Post: Test Post>'])


class PostDetailViewTests(TestCase):
    def test_post_detail_view_with_existing_post(self):
        # Create test data
        author = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', text='Test Content', author=author, published_date=timezone.now())

        response = self.client.get(reverse('post_detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], post)


    def test_post_detail_view_with_nonexistent_post(self):
        response = self.client.get(reverse('post_detail', args=[999]))  # Assuming post with pk=999 does not exist
        self.assertEqual(response.status_code, 404)


class PostNewViewTests(TestCase):
    def test_post_new_view_with_valid_data(self):
        # Login to create a new post
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('post_new'), {'title': 'New Post', 'text': 'New Content'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful post creation

        # Check if the post is created and associated with the logged-in user
        self.assertTrue(Post.objects.filter(title='New Post', text='New Content', author__username='testuser').exists())


    def test_post_new_view_with_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('post_new'), {'title': ''})  # Invalid data, expecting form errors
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')


class PostEditViewTests(TestCase):
    def test_post_edit_view_with_valid_data(self):
        # Create test data
        author = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', text='Test Content', author=author, published_date=timezone.now())

        # Login to edit the post
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('post_edit', args=[post.pk]), {'title': 'Edited Post'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful post edit

        # Check if the post is edited
        edited_post = Post.objects.get(pk=post.pk)
        self.assertEqual(edited_post.title, 'Edited Post')

    def test_post_edit_view_with_invalid_data(self):
        # Create test data
        author = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', text='Test Content', author=author, published_date=timezone.now())

        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('post_edit', args=[post.pk]), {'title': ''})  # Invalid data, expecting form errors
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'title', 'This field is required.')

class BlogHomeViewTests(TestCase):
    def test_blog_home_view(self):
        response = self.client.get(reverse('blog_home'))


