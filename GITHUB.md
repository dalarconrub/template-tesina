# Subir este proyecto a GitHub

El repositorio local ya está inicializado con un commit. Para guardarlo en GitHub:

## 1. Crear el repositorio en GitHub

1. Entra en [github.com/new](https://github.com/new).
2. Elige un nombre (por ejemplo: `template-tesina` o `tesina-template`).
3. **No** marques "Add a README" ni ".gitignore" (ya los tienes aquí).
4. Clic en **Create repository**.

## 2. Conectar y subir desde tu PC

En la terminal, desde la carpeta del proyecto (`template_paper`), ejecuta (sustituye `TU_USUARIO` y `NOMBRE_REPO` por los tuyos):

```bash
git branch -M main
git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git
git push -u origin main
```

Si usas SSH:

```bash
git remote add origin git@github.com:TU_USUARIO/NOMBRE_REPO.git
git push -u origin main
```

Si GitHub te pide identificación, usa un token de acceso personal (Settings → Developer settings → Personal access tokens) en lugar de la contraseña.
