class OrganizationQuerysetMixin:

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(organization=self.request.user.organization)

class OrganizationCreateMixin:

    def form_valid(self, form):
        form.instance.organization = self.request.user.organization
        return super().form_valid(form)
