drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title next not null,
  'text' text not null
);
