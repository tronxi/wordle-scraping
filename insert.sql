SET SQL_SAFE_UPDATES = 0;
insert into wordle.word(id, day, word) SELECT next_val, DATE_ADD('2022-01-25', INTERVAL next_val DAY), "gripe" FROM wordle.hibernate_sequence;
update wordle.hibernate_sequence set next_val = next_val + 1;