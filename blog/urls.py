from django.urls import path
from .views import blog, blog2, create_blog, updateBlog, deleteBlog, areaview, create_area, updateArea, deleteArea


urlpatterns = [
    path('blog/', blog),
    path('blog2/', blog2),
    path ('create/', create_blog),
    path ('update/<int:id>/', updateBlog),
    path ('delete/<int:id>/', deleteBlog),
    path ('area/', areaview),
    path ('CreateArea/', create_area ),
    path ('updateArea/<int:id>', updateArea),
    path ('deleteArea/<int:id>', deleteArea)

]
