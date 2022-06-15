
# class CreateCommentLection(View):
#     # def get(self, request):
#     #     form = CommentLectionForm()
#     #     return render(request, 'badphilosopher/detailed_answer.html', context={'form': form})
#
#     def post(selfs, request, current_post):
#         form = CommentLectionForm(request.POST)
#         current_post_obj = Lections.objects.get(number=current_post)
#         if form.is_valid():
#             # Обработка данных из form.cleaned_data
#             form = form.save(commit=False)
#             form.post = current_post_obj
#             form.save()
#             return redirect(current_post_obj.get_absolute_url())
#         else:
#             print("Хочу быть тут")
#             form = CommentLectionForm(request.POST)
#         return render(request, 'badphilosopher/detailed_answer.html', context={"answer" : current_post_obj, 'form' : form})
