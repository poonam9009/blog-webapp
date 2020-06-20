from django.shortcuts import render,HttpResponse,redirect
from blog.models import BlogAppPost,Comments
from django.contrib import messages
from blog.templatetags import get_dict


# Create your views here.
def bloghome(request):
    allpost = BlogAppPost.objects.all()
    context = {'allpost':allpost}
    return render(request,'blog/bloghome.html', {'allpost':allpost} )


def blogpost(request,slug):
    post = BlogAppPost.objects.filter(slug = slug).first()
    # post.views = post.views + 1
    comments = Comments.objects.filter(post = post, parent = None)
    replies = Comments.objects.filter(post = post,).exclude(parent =None)
    replydict ={}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno] = [reply]
        else:
            replydict[reply.parent.sno].append(reply)
    post.save()
    context = {'post': post, 'comments':comments , 'replies':replies , 'replydict':replydict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = BlogAppPost.objects.get(sno=postSno)
        parent = request.POST.get('parent')
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = Comments(comment =comment, post=post, user=user)
            messages.success(request,"Your comment has been sent successfully.")
        else :
            parent = Comments.objects.get(sno = parentSno)
            comment = Comments(comment =comment, post=post, user=user, parent=parent)
            messages.success(request,"Your reply has been sent successfully.")

        comment.save()
        # messages.success(request,"Your comment has been sent successfully.")
    return redirect(f'/blog/{post.slug}')
