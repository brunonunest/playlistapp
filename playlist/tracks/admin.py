from django.contrib import admin
from .models import Track, Producer, Label


class TrackinLine(admin.TabularInline):
    model = Track.producer.through
    extra = 1


class LabelinLine(admin.TabularInline):
    model = Label
    extra = 1


class ProducerAdmin(admin.ModelAdmin):
    inlines = [LabelinLine, TrackinLine]
    list_display = ('name', 'link',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'link',
            )
        }),
    )


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'link','producers')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'link',
                'producers',
            )
        }),
    )


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'producers')
    list_display_links = ('name',)
    list_filter = ('name', 'producer')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'link',
                'producer',
            )
        }),
    )


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Label, LabelAdmin)




#admin.site.register(Track)
#admin.site.register(Producer)
#admin.site.register(Label)

