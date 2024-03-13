# Merge Images into TIFF Script

Этот скрипт предназначен для объединения изображений из нескольких папок в один файл формата TIFF.

## Как использовать

1. Поместите изображения, которые вы хотите объединить, в разные папки.

2. Укажите имена этих папок в виде списка `folder_names` в коде скрипта, заменив их значения в квадратных скобках в строке, начинающейся с `folder_names = [...]`.

3. Укажите имя файла, в который будут сохранены объединенные изображения, в переменной `output_filename` в коде скрипта.

4. Запустите скрипт, выполните его, и в результате будет создан файл TIFF, содержащий все изображения из указанных папок.

Обратите внимание, что скрипт поддерживает изображения в форматах JPEG, PNG и BMP.