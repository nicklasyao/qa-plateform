cd front-end
rd dist /s /q
call cnpm install
call cnpm run build
cd ..
rd back-server\static /s /q
mkdir back-server\static
del back-server\templates\index.html
xcopy front-end\dist\static back-server\static /s /e /c /y /h /r
copy front-end\dist\index.html back-server\templates\index.html