from django.template import Context, loader
from django.http import HttpResponse
from models import Blog, Comment
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def blog_list(request, limit=100):
	blog_list = Blog.objects.all()
	print type(blog_list)
	print blog_list
	#return HttpResponse('going to give a list')
	t = loader.get_template('blog/list.html')
	c = Context({'blog_list':blog_list})
	return HttpResponse(t.render(c))

class CommentForm(ModelForm):
	class Meta:
		exclude=['comment_title']		
		model = Comment
		fields = ('comment_title','comment_author','comment_body','comment_created', 'comment_updated')
	def commform(self):
		print comment
		return self.fields
@csrf_exempt
#def comment_edit(request, id, showComments=False):
	
#	comm = Blog.objects.get(id=id)
#	print blog
#	if showComments:
#		comments = Comment.objects.filter(comment_title__comm.id=id)
#		print comments
#	if request.method == 'POST':
#		comment = Comment(comment_title=comm)
#		form = CommentForm(request.POST, instance=comment)
#		if form.is_valid():
#			form.save()
#			print form
#			return HttpResponseRedirect(request.path)
#	else:
#		form = CommentForm()
		
#	loadedit = loader.get_template('blog/editcomment.html')
#	dispedit = Context({'blog':blog, 'comments':comments,'form':form.as_p()})
#	return HttpResponse(loadedit.render(dispedit))
@csrf_exempt
def blog_detail(request, id, showComments=False):
	blog = Blog.objects.get(id=id)
	print blog
	if showComments:
		comments = Comment.objects.filter(comment_title__id=id)
		print comments
	if request.method == 'POST':
		comment = Comment(comment_title=blog)
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			print form
			return HttpResponseRedirect(request.path)
	else:
		form = CommentForm()
	
	#return HttpResponse('it should work')
	loaddetail = loader.get_template('blog/detail.html')
	dispdetail = Context({'blog':blog, 'comments':comments,'form':form.as_p()})
	return HttpResponse(loaddetail.render(dispdetail))
	
def blog_search(request, term):
	r = Blog.objects.filter(title__icontains='term')
	print r
	#loadsearch = loader.get_template('/blog/search.html')
	#dispsearch = Context({'term':term})
	return HttpResponse(term)

def home(request):
	t = loader.get_template('blog/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

