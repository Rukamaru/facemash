from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Question
from .models import Choice
from .models import User
from .models import Photo

admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Photo)


class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("question_text",)}
    fieldsets = [
        ('Mise en ligne', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question',      {'fields': ['question_text', 'slug', 'choice']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
