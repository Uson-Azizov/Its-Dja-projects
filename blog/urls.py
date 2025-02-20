from django.urls import path
from .views import blog, blog2, create_blog, updateBlog, deleteBlog, areaview, create_area, updateArea, deleteArea, RegionView, CreateRegion, commentView,deleteComment


urlpatterns = [
    path('', blog, name='blog'),
    path('blog2/', blog2),
    path('create/', create_blog),
    path('update/<int:id>/', updateBlog),
    path('delete/<int:id>/', deleteBlog),
    path('area/', areaview),
    path('CreateArea/', create_area ),
    path('updateArea/<int:id>', updateArea),
    path('deleteArea/<int:id>', deleteArea),
    path('regions/', RegionView),
    path('CreateRegion/', CreateRegion),
    path('comment/<int:id>/', commentView, name='comment_view'),
    path('CommentDelete/<int:id>/', deleteComment,name='delete_comment'),

]







