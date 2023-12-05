from django import forms
from django.conf import settings
from .models import Offer
from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html



class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['title', 'description', 'timeline', 'budget', 'attached_files']

        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = "Project Title"
        self.fields['description'].label = "How can we help you?"
        self.fields['timeline'].label = "What's your timeline?"
        self.fields['budget'].label = "What's your budget range?"
        self.fields['attached_files'].label = 'Attach Files(Optional)'
        
        
        # Add classes to the fields
        self.fields['title'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['description'].widget.attrs.update({'class': 'offer_form_area_input_classes', 'rows': '4'})
        self.fields['attached_files'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['timeline'].widget.attrs.update({'class': 'offer_form_input_classes'})
        self.fields['budget'].widget.attrs.update({'class': 'offer_form_input_classes'})





class CustomPayPalPaymentsForm(PayPalPaymentsForm):
    def as_p(self):
        return format_html(
            """<form action="{0}" method="post">
            {1}
            <button type="submit" class="bg-black dark:bg-white hover:bg-slate-950 hover:dark:bg-slate-50 px-20 exsm:px-24 rounded py-2.5 m-auto flex justify-center items-center">
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="150" height="40" viewBox="-11.153 -13.144 326.05 105.914" id="paypal"><g transform="matrix(2.07675 0 0 -2.07675 -11.153 92.77)"><defs><path id="a" d="M-84.525-27.457h326.05V78.457h-326.05z"></path></defs><clipPath id="b"><use overflow="visible" xlink:href="#a"></use></clipPath><g clip-path="url(#b)"><path fill="#003087" d="M32.419 40.982c-1.674 1.908-4.7 2.726-8.571 2.726H12.613a1.609 1.609 0 0 1-1.59-1.357L6.347 12.68a.964.964 0 0 1 .953-1.114h6.936l1.742 11.049-.054-.346a1.604 1.604 0 0 0 1.583 1.357h3.296c6.475 0 11.545 2.63 13.026 10.238.044.225.082.444.115.658.44 2.812-.003 4.726-1.524 6.459"></path><path fill="#009cde" d="M117.331 26.863c-.424-2.784-2.55-2.784-4.606-2.784h-1.17l.821 5.198c.05.314.32.545.638.545h.537c1.4 0 2.722 0 3.404-.797.407-.477.53-1.185.376-2.162m-.895 7.264h-7.756a1.08 1.08 0 0 1-1.066-.91L104.48 13.33a.647.647 0 0 1 .638-.747h3.98c.371 0 .687.27.745.636l.89 5.64c.082.523.534.91 1.064.91h2.454c5.11 0 8.058 2.471 8.828 7.372.347 2.142.014 3.826-.989 5.005-1.103 1.296-3.058 1.982-5.653 1.982"></path><path fill="#003087" d="M62.011 26.863c-.424-2.784-2.55-2.784-4.607-2.784h-1.17l.821 5.198c.05.314.32.545.638.545h.537c1.4 0 2.722 0 3.404-.797.408-.477.531-1.185.377-2.162m-.895 7.264H53.36c-.53 0-.982-.386-1.065-.91L49.16 13.33a.646.646 0 0 1 .638-.747h3.704c.53 0 .981.386 1.064.91l.847 5.365c.082.524.534.91 1.064.91h2.454c5.11 0 8.058 2.472 8.828 7.373.347 2.142.014 3.826-.989 5.005-1.103 1.296-3.058 1.982-5.653 1.982M79.123 19.723c-.36-2.122-2.043-3.547-4.192-3.547-1.077 0-1.94.347-2.494 1.003-.55.65-.756 1.577-.582 2.608.334 2.104 2.046 3.574 4.162 3.574 1.055 0 1.91-.35 2.476-1.012.569-.667.793-1.599.63-2.626m5.176 7.23h-3.714a.647.647 0 0 1-.64-.547l-.162-1.038-.26.376c-.804 1.167-2.597 1.558-4.387 1.558-4.103 0-7.608-3.11-8.29-7.47-.355-2.177.149-4.256 1.383-5.707 1.133-1.333 2.75-1.888 4.677-1.888 3.308 0 5.142 2.124 5.142 2.124l-.166-1.032a.646.646 0 0 1 .639-.747h3.344c.53 0 .982.385 1.065.91l2.008 12.713a.647.647 0 0 1-.64.747"></path><path fill="#009cde" d="M134.443 19.723c-.36-2.122-2.043-3.547-4.192-3.547-1.077 0-1.94.347-2.494 1.003-.55.65-.756 1.577-.582 2.608.334 2.104 2.045 3.574 4.162 3.574 1.055 0 1.91-.35 2.476-1.012.569-.667.793-1.599.63-2.626m5.176 7.23h-3.714a.647.647 0 0 1-.64-.547l-.162-1.038-.26.376c-.804 1.167-2.597 1.558-4.387 1.558-4.102 0-7.607-3.11-8.29-7.47-.355-2.177.15-4.256 1.384-5.707 1.133-1.333 2.75-1.888 4.677-1.888 3.309 0 5.143 2.124 5.143 2.124l-.166-1.032a.644.644 0 0 1 .637-.747h3.343c.53 0 .982.385 1.066.91l2.008 12.713a.647.647 0 0 1-.64.747"></path><path fill="#003087" d="M104.08 26.952h-3.734c-.357 0-.69-.177-.89-.473l-5.15-7.584-2.183 7.288a1.08 1.08 0 0 1-1.033.77h-3.669a.647.647 0 0 1-.612-.856l4.11-12.066-3.866-5.455a.647.647 0 0 1 .528-1.02h3.73c.352 0 .683.173.885.463l12.414 17.918a.646.646 0 0 1-.53 1.015"></path><path fill="#009cde" d="M143.996 33.58l-3.184-20.251a.647.647 0 0 1 .639-.747h3.201c.53 0 .982.386 1.065.91l3.139 19.888a.646.646 0 0 1-.639.747h-3.582a.645.645 0 0 1-.639-.546"></path><path fill="#003087" d="M32.419 40.982c-1.674 1.908-4.7 2.726-8.571 2.726H12.613a1.609 1.609 0 0 1-1.59-1.357L6.347 12.68a.964.964 0 0 1 .953-1.114h6.936l1.742 11.049-.054-.346a1.604 1.604 0 0 0 1.583 1.357h3.296c6.475 0 11.545 2.63 13.026 10.238.044.225.082.444.115.658.44 2.812-.003 4.726-1.524 6.459"></path><path fill="#003087" d="M17.849 34.485a1.408 1.408 0 0 0 1.389 1.187h8.808c1.043 0 2.016-.068 2.905-.21a12.206 12.206 0 0 0 1.44-.322 7.957 7.957 0 0 0 1.551-.618c.442 2.813-.002 4.726-1.523 6.46-1.675 1.907-4.7 2.725-8.571 2.725H12.612a1.609 1.609 0 0 1-1.588-1.357L6.346 12.682a.964.964 0 0 1 .952-1.115h6.937l1.742 11.05 1.872 11.868z"></path><path fill="#009cde" d="M33.943 34.523a18.294 18.294 0 0 0-.115-.658c-1.481-7.607-6.551-10.238-13.026-10.238h-3.297a1.602 1.602 0 0 1-1.582-1.357l-1.688-10.702-.48-3.036a.844.844 0 0 1 .834-.976h5.847c.692 0 1.28.504 1.389 1.187l.057.298 1.102 6.984.07.386a1.407 1.407 0 0 0 1.39 1.187h.875c5.664 0 10.099 2.3 11.395 8.956.54 2.78.26 5.103-1.17 6.734a5.584 5.584 0 0 1-1.601 1.235"></path><path fill="#012169" d="M32.392 35.14c-.226.067-.459.127-.699.18-.24.053-.488.1-.742.14-.89.145-1.862.213-2.906.213h-8.807a1.404 1.404 0 0 1-1.389-1.188l-1.872-11.87-.054-.345a1.602 1.602 0 0 0 1.582 1.357h3.297c6.475 0 11.545 2.63 13.026 10.238.044.225.081.443.115.658a7.998 7.998 0 0 1-1.218.514c-.109.036-.22.07-.333.104"></path></g></g></svg>
            </button>
        </form>""",
            self.get_login_url(),
            super().as_p(),
        )
        
    def get_image(self):
        return None



