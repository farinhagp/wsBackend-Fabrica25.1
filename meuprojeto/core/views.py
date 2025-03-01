from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Usuario, Perfil


def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'core/usuario_list.html', {'usuarios': usuarios})


def usuario_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()

        # Verifica se os campos estão preenchidos
        if not nome or not email:
            messages.error(request, "Nome e e-mail são obrigatórios.")
            return redirect('usuario_create')

        # Valida formato do e-mail
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "E-mail inválido. Digite um e-mail válido.")
            return redirect('usuario_create')

        # Verifica se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Este e-mail já está em uso. Escolha outro.")
            return redirect('usuario_create')

        try:
            usuario = Usuario.objects.create(nome=nome, email=email)
            avatar_seed = "".join(e for e in nome if e.isalnum())
            avatar_url = f"https://api.dicebear.com/7.x/pixel-art/svg?seed={avatar_seed}"
            Perfil.objects.create(usuario=usuario, avatar_url=avatar_url)

            messages.success(request, "Usuário criado com sucesso!")
            return redirect('usuario_list')
        except Exception as e:
            messages.error(request, f"Erro ao criar usuário: {e}")
            return redirect('usuario_create')

    return render(request, 'core/usuario_form.html')


def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()

        if not nome or not email:
            messages.error(request, "Nome e e-mail são obrigatórios.")
            return redirect('usuario_update', pk=pk)

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "E-mail inválido. Digite um e-mail válido.")
            return redirect('usuario_update', pk=pk)

        if Usuario.objects.filter(email=email).exclude(pk=pk).exists():
            messages.error(request, "Este e-mail já está em uso. Escolha outro.")
            return redirect('usuario_update', pk=pk)

        try:
            usuario.nome = nome
            usuario.email = email
            usuario.save()

            usuario.perfil.avatar_url = f"https://api.dicebear.com/7.x/pixel-art/svg?seed={''.join(e for e in nome if e.isalnum())}"
            usuario.perfil.save()

            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('usuario_list')
        except Exception as e:
            messages.error(request, f"Erro ao atualizar usuário: {e}")
            return redirect('usuario_update', pk=pk)

    return render(request, 'core/usuario_form.html', {'usuario': usuario})


def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        try:
            usuario.delete()
            messages.success(request, "Usuário excluído com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao excluir usuário: {e}")
        return redirect('usuario_list')
    return render(request, 'core/usuario_confirm_delete.html', {'usuario': usuario})
