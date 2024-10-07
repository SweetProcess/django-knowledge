from django.contrib import admin

from knowledge.models import Question, Response, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
    list_select_related = True
    raw_id_fields = ['user']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Response._meta.fields]
    list_select_related = True
    raw_id_fields = ['user', 'question']
