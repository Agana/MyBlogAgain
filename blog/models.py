from django.contrib import admin

from django.db import models

from django.db import models
class Blog(models.Model):
	title= models.CharField(max_length=60)
	body= models.TextField()
	created= models.DateField()
	updated= models.DateField()
	def __unicode__(self):
		return self.title
class Comment(models.Model):
	comment_title = models.ForeignKey('Blog')
	comment_body= models.TextField()
	comment_author= models.CharField(max_length=60)
	comment_created= models.DateField()
	comment_updated= models.DateField()
	def body_first_sixty(self):
		return self.title[:60]
        def __unicode__(self):
		return self.comment_author
	
#Extending the admin interface

class CommentInline(admin.TabularInline):
        model = Comment
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'updated')
	search_fields = ('title', 'body')
	list_filter = ('title','created')
	inlines = [CommentInline]
class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment_title', 'comment_author','body_first_sixty','comment_created','comment_updated')
	list_filter = ('comment_created','comment_author')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)




