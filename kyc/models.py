from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


def kycDocumentImage(instance, filename):
    return '/'.join( ['prductsubcategory', str(instance.id), filename] )


APPLICATION_STATE=(
    ('pending','pending'),
    ('approved','approved'),
    ('rejected','rejected'),
)


class KYCDocumentType(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class KYCDocument(models.Model):
    type = models.ForeignKey(KYCDocumentType, on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to=kycDocumentImage,
        max_length=254
    )

class KYCApplication(models.Model):
    user = models.ForeignKey(User, related_name='kycApplication' ,on_delete=models.CASCADE)
    status = models.IntegerField(choices=APPLICATION_STATE, default='pending')
    rejection_reason = models.TextField(null=True)
    document = models.ForeignKey(KYCDocument, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)