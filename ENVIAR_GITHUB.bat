@echo off
title Enviar Projeto para o GitHub - Citizen Assist AI
echo ========================================================
echo       ENVIAR PROJETO PARA O GITHUB (FIAP GS 2026.2)
echo ========================================================
echo.
echo 1. Va em https://github.com/new e crie um repositorio (ex: citizen-assist-ai)
echo    * Nao precisa marcar README, .gitignore ou License (ja estao prontos aqui!)
echo.
echo 2. Copie a URL do seu repositorio recem-criado.
echo    Exemplo: https://github.com/SEU_USUARIO/citizen-assist-ai.git
echo.
set /p REPO_URL="Cole a URL do seu repositorio do GitHub aqui: "

if "%REPO_URL%"=="" (
    echo [ERRO] Nenhuma URL informada. Tente novamente.
    pause
    exit /b
)

echo.
echo Configurando repositorio remoto...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo.
echo Enviando arquivos para o GitHub...
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo      SUCESSO! Seu projeto esta publicado no GitHub!
    echo ========================================================
) else (
    echo [ATENCAO] Se pediu login, autentique sua conta do GitHub na janela do navegador.
)

pause
