SELECT 
authors.name, books.title, series.name, custom_column_1.value, tags.name, languages.lang_code
FROM
authors, books, series, custom_column_1, tags, languages, books_series_link, books_custom_column_1_link, books_tags_link, books_languages_link
WHERE 
(authors.sort = books.author_sort) and 
(books.id = books_series_link.book and series.id = books_series_link.series) and
(books.id = books_custom_column_1_link.book and custom_column_1.id =  books_custom_column_1_link.value) and
(books.id = books_tags_link.book and tags.id = books_tags_link.tag) and
(books.id = books_languages_link.book and languages.id = books_languages_link.lang_code)



OKŁADKA(MINI), AUTOR, TYTUŁ, CYKL, GATUNEK, TAGI, JĘZYK
