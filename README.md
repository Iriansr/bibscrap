# Bibscrap
Small script which generates a .txt (new.txt) file suitable for using it as a .bib for LATEX using selenium for scrapping in https://www.doi2bib.org/.

What do u need?
* Gecko driver https://github.com/mozilla/geckodriver/releases.
* A .txt file with the same format as dois.txt:
  - First line with the atributes you wanna add to your LATEX bibliography, separated by commas.
  - Following lines with the DOIs of the bibliography you used.

This script is intended for unix based systems w/ firefox but it is portable to windows and other drivers by using a different driver.
