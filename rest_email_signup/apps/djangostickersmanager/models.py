from django.db import models

class StickerData(models.Model):
    item_userstickerset = models.FileField(blank=False, null=False)
    sticker_title = models.CharField(max_length=20)
    sticker_desc = models.CharField(max_length=200)
    userid = models.CharField(max_length=20)
    sticker_id = models.CharField(max_length=20)
    is_public = models.BooleanField(default=False)
    class Meta:
        db_table = "stickerdata_table"
