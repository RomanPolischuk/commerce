from django.contrib import admin

from .models import Auction, Bid, Comment, Group, User

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ('id','last_login','is_superuser','username','first_name',
    'last_name', 'email','is_staff','is_active', )

class AdminAuction(admin.ModelAdmin):
    list_display =  ('id', 'name', 'description', 'price', 'link_to_foto', 'group', 'active_auction',)

class AdminBid(admin.ModelAdmin):
    list_display =('id', 'bid', 'user', 'auction',)

class AdminComment(admin.ModelAdmin):
    list_display =('id', 'comment', 'user', 'auction',)

class AdminGroup(admin.ModelAdmin):
    list_display =('id', 'name', )


admin.site.register(User,AdminUser)
admin.site.register(Auction)
admin.site.register(Comment, AdminComment)
admin.site.register(Bid, AdminBid)
admin.site.register(Group, AdminGroup)


