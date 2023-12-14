-- creates a trigger that decreases the quantity
-- of an item after adding a new order
CREATE TRIGGER update_item_quantity
AFTER INSERT ON order
FOR EACH ROW
  BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
  END;
