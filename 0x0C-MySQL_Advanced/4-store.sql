-- SQL script
-- creates a trigger that decreases quantity of an item after adding order
CREATE
TRIGGER reduce_item AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
