from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能少于5个字符'
                            })
    desc = forms.CharField(min_length=20, required=True,
                           error_messages={
                               'required': '文章描述是必填项',
                               'min_length': '文章描述不能少于20个字符'
                           }
                           )
    # content = forms.Textarea()
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必填项'
                              }
                              )


class AddItemForm(forms.Form):
    name = forms.CharField(required=True,
                           error_messages={
                               'required': '栏目名称是必填项'
                           })
    alias = forms.CharField(required=True,
                            error_messages={
                                'required': '栏目别名是必填项'
                            })
    describe = forms.CharField(required=True,
                               error_messages={
                                   'required': '描述是必填项'
                               })
