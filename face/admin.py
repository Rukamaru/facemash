from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Question, Choice, Photo  #, User

admin.site.register(Choice)
# admin.site.register(User)
admin.site.register(Photo)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("question_text",)}
    fieldsets = [
        ('Mise en ligne', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Question',      {'fields': ['author', 'question_text', 'slug']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)