from django.db import models

# Create your models here.
class Blog(models.Model):
      blog_title = models.CharField(max_length=100)
      blog_body = models.TextField()
      class Meta:
            db_table = 'blogs'

      def __str__(self):
        return self.blog_title
      
class Comment(models.Model):
      blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
      comment_body=models.TextField()

      class Meta:
            db_table = 'comments'

      def __str__(self):
        return self.comment_body