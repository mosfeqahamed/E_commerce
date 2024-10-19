from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        # Resize image before saving
        if self.image:
            img = Image.open(self.image)
            output_size = (300, 300)  # You can adjust the size as needed
            img = img.resize(output_size, Image.LANCZOS)

            # Save the resized image to a BytesIO object
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG')

            # Use the BytesIO object to create a new Django file object
            self.image = File(thumb_io, name=self.image.name)
        
        super().save(*args, **kwargs)

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
