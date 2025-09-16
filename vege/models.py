from django.db import models
from django.contrib.auth.models import User




class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null = True , blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    receipe_view_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.receipe_name
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipe = models.ForeignKey(Receipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user' , 'receipe')  #user can like only once
        
    def __str__(self):
        return f"{self.user.username} likes {self.receipe.receipe_name}" 
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipe = models.ForeignKey(Receipe, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.receipe.receipe_name}"
    