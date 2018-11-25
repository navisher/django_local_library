from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)

# Define the admin class
class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the admin class for book using the decortor
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    model.extra=0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

# Register the admin class for bookinstance using the decortor
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id') 
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )




