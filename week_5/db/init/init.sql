CREATE TABLE IF NOT EXISTS Meals (
    MealId SERIAL PRIMARY KEY
    ,MealName TEXT NOT NULL
    ,MealPrice DECIMAL(10,2) NOT NULL
);

INSERT INTO Meals (MealName, MealPrice) VALUES ('Lemon-Garlic Shrimp',37.90);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Grilled chicken Burger',35.90);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Chicken Taquitas',33.80);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Chicken Pasta',37.90);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Little House Salad',7.90);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Stuffed Mushrooms',22.55);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Beet and Avocado Salad',20.10);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Chicken Samosas',10.10);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Dynamite Shrimp',7.25);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Chicken Pot Stickers',17.25);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Asian Chicken Lettuce Wrap Tacos',12.55);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Crispy Brussels Sprouts',8.99);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Lemon-Herb Parmesan Chicken',33.90);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Grilled Salmon',20.10);
INSERT INTO Meals (MealName, MealPrice) VALUES ('Grilled Steak Medallions',45.22);
