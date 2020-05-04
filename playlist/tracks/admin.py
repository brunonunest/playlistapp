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
    list_display_links = ('name', 'link',)
    #list_editable =
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


    def combine_name_producer(self, obj):
        return "{} - {}".format(obj.name, obj.producer)


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Track)
admin.site.register(Label)




#admin.site.register(Track)
#admin.site.register(Producer)
#admin.site.register(Label)

