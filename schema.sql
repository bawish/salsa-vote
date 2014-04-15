CREATE TABLE IF NOT EXISTS salsas (
  salsa_id integer primary key autoincrement,
  salsa_url text not null,
  type text not null
);

CREATE TABLE IF NOT EXISTS users (
  user_id integer primary key autoincrement,
  user_email text not null
);

CREATE TABLE IF NOT EXISTS votes (
  vote_id integer primary key autoincrement,
  user_id integer not null,
  salsa_id integer not null,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (salsa_id) REFERENCES salsas(salsa_id)
);
