-- SQL script
-- Creates an index on table names and first letter of name and its score  
CREATE INDEX idx_name_first_score ON names (name(1), score);
