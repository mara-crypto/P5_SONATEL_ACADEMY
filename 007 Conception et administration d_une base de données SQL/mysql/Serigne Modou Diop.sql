--EXERCICE1

                --1ER CAS
CREATE DATABASE Piece_vehicule;
USE Piece_vehicule;
CREATE TABLE Vehicule (
    id_vehicule              INT(7) AUTO_INCREMENT PRIMARY KEY,
    marque                   VARCHAR(15),
    modele                   VARCHAR(15),
    annee                    INT(4)
);

CREATE TABLE Reference (
    id_ref                  INT(7) AUTO_INCREMENT PRIMARY KEY,
    code_ref                VARCHAR(15),
    prix_vente              INT
);

CREATE TABLE Categorie (
    id_cat                  INT(7) AUTO_INCREMENT PRIMARY KEY,
    code_cat                VARCHAR(7),
    nom_cat                 VARCHAR(15)
);

CREATE TABLE Piece (
    id_piece                INT(7) AUTO_INCREMENT PRIMARY KEY,
    date_recuparation       DATE,
    id_cat                  INT,
    id_ref                  INT,
    FOREIGN KEY (id_cat) REFERENCES Categorie(id_cat), 
    FOREIGN KEY (id_ref) REFERENCES Reference(id_ref)
);

CREATE TABLE Correspondance_vehicule_piece (
    id_vehicule                 INT,
    id_piece                    INT,
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule),
    FOREIGN KEY (id_piece) REFERENCES Piece(id_piece)
);


-- Insérer des données dans la table Vehicule
INSERT INTO Vehicule (marque, modele, annee) VALUES ('Mercedes', 'AMG', '2021')
INSERT INTO Vehicule (marque, modele, annee)
VALUES
    ('Renault', 'Clio', 2010),
    ('Peugeot', '308', 2015),
    ('Volkswagen', 'Golf', 2018);

-- Insérer des données dans la table Reference
INSERT INTO Reference (code_ref, prix_vente)
VALUES
    ('REF-001', 50),
    ('REF-002', 80),
    ('REF-003', 120);

-- Insérer des données dans la table Categorie
INSERT INTO Categorie (code_cat, nom_cat)
VALUES
    ('CAT-001', 'Moteur'),
    ('CAT-002', 'Freinage'),
    ('CAT-003', 'Suspension');

-- Insérer des données dans la table Piece
INSERT INTO Piece (date_recuparation, id_cat, id_ref)
VALUES
    ('2022-01-05', 1, 1),
    ('2022-02-10', 2, 2),
    ('2022-03-15', 3, 3);

-- Insérer des données dans la table Correspondance_vehicule_piece
INSERT INTO Correspondance_vehicule_piece (id_vehicule, id_piece)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);
--FIN MERCI



--2EME CAS

CREATE DATABASE cas2;
USE Piece_vehicule_cas2;

CREATE TABLE Vehicule (
    id_vehicule         INT(7) AUTO_INCREMENT PRIMARY KEY,
    marque              VARCHAR(15),
    modele              VARCHAR(15),
    annee               INT(4)
);

CREATE TABLE Categorie (
    id_cat              INT(7) AUTO_INCREMENT PRIMARY KEY,
    code_cat            VARCHAR(7),
    nom_cat             VARCHAR(15)
);

CREATE TABLE Piece (
    id_piece            INT(7) AUTO_INCREMENT PRIMARY KEY,
    code_reference      VARCHAR(15),
    prix_vente          INT,
    date_recuparation   DATE,
    id_cat              INT(7),
    FOREIGN KEY (id_cat) REFERENCES Categorie(id_cat)
);

CREATE TABLE Correspondance_vehicule_piece (
    id_vehicule         INT(7),
    id_piece            INT(7),
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule),
    FOREIGN KEY (id_piece) REFERENCES Piece(id_piece)
);




--EXERCICE 2

--CAS 1

CREATE DATABASE Bibliotheque1;
use Bibliotheque1;

CREATE TABLE Auteur (
    id_aut              INT AUTO_INCREMENT PRIMARY KEY,
    nom_aut             VARCHAR(15),
    prenom_aut          VARCHAR(15)
);

CREATE TABLE Adherent (
    id_ad               INT AUTO_INCREMENT PRIMARY KEY,
    nom_ad              VARCHAR(15),
    prenom_ad           VARCHAR(15),
    adresse_ad          VARCHAR(15),
    tel_ad              INT(9)
);

CREATE TABLE Mot_cle (
    id_mc               INT AUTO_INCREMENT PRIMARY KEY,
    nom_mc              VARCHAR(15)
);

CREATE TABLE Rayon (
    id_rayon            INT AUTO_INCREMENT PRIMARY KEY,
    nom_rayon           VARCHAR(15)
);

CREATE TABLE Ouvrage (
    id_ouvrage          INT AUTO_INCREMENT PRIMARY KEY,
    titre               VARCHAR(15),
    id_rayon            INT,
    id_ad               INT,
    FOREIGN KEY (id_rayon) REFERENCES Rayon (id_rayon),
    FOREIGN KEY (id_ad) REFERENCES Adherent (id_ad)
);


CREATE TABLE Rediger (
    id_aut              INT,
    id_ouvrage          INT,
    FOREIGN KEY (id_aut) REFERENCES Auteur (id_aut), 
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage) 
);

CREATE TABLE Referencer (
    id_ouvrage          INT,
    id_mc               INT,
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage),
    FOREIGN KEY (id_mc) REFERENCES Mot_cle (id_mc)
);

INSERT INTO Auteur (nom_aut, prenom_aut) VALUES ('Hugo', 'Victor');
INSERT INTO Auteur (nom_aut, prenom_aut) VALUES ('Camus', 'Albert');
INSERT INTO Auteur (nom_aut, prenom_aut) VALUES ('Zola', 'Emile');

INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES ('Mbaye', 'Djily', 'Parcelle', 771231234);
INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES ('Top', 'Daour', '26', 781232342);
INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES ('Diop', 'Serigne Modou', 'Yoff', 771122941);

INSERT INTO Mot_cle (nom_mc) VALUES ('Roman');
INSERT INTO Mot_cle (nom_mc) VALUES ('Thriller');
INSERT INTO Mot_cle (nom_mc) VALUES ('Science-fiction');

INSERT INTO Rayon (nom_rayon) VALUES ('Littérature');
INSERT INTO Rayon (nom_rayon) VALUES ('Policier');
INSERT INTO Rayon (nom_rayon) VALUES ('Science-fiction');

INSERT INTO Ouvrage (titre, id_rayon, id_ad) VALUES ('Les Misérables', 1, 1);
INSERT INTO Ouvrage (titre, id_rayon, id_ad) VALUES ("L'Étranger", 2, 2);
INSERT INTO Ouvrage (titre, id_rayon, id_ad) VALUES ('Germinal', 1, 3);

INSERT INTO Rediger (id_aut, id_ouvrage) VALUES (1, 4);--
INSERT INTO Rediger (id_aut, id_ouvrage) VALUES (2, 2);
INSERT INTO Rediger (id_aut, id_ouvrage) VALUES (3, 3);

INSERT INTO Referencer (id_ouvrage, id_mc) VALUES (5, 1);--
INSERT INTO Referencer (id_ouvrage, id_mc) VALUES (2, 1);
INSERT INTO Referencer (id_ouvrage, id_mc) VALUES (3, 1);



--CAS 2

CREATE DATABASE Bibliotheque2;
use Bibliotheque2;

CREATE TABLE Auteur (
    id_aut              INT AUTO_INCREMENT PRIMARY KEY,
    nom_aut             VARCHAR(15),
    prenom_aut          VARCHAR(15)
);

CREATE TABLE Adherent (
    id_ad               INT AUTO_INCREMENT PRIMARY KEY,
    nom_ad              VARCHAR(15),
    prenom_ad           VARCHAR(15),
    adresse_ad          VARCHAR(15),
    tel_ad              INT(9)
);

CREATE TABLE Mot_cle (
    id_mc               INT AUTO_INCREMENT PRIMARY KEY,
    nom_mc              VARCHAR(15)
);

CREATE TABLE Rayon (
    id_rayon            INT AUTO_INCREMENT PRIMARY KEY,
    nom_rayon           VARCHAR(15)
);

CREATE TABLE Ouvrage (
    id_ouvrage          INT AUTO_INCREMENT PRIMARY KEY,
    titre               VARCHAR(15),
    id_rayon            INT,
    FOREIGN KEY (id_rayon) REFERENCES Rayon (id_rayon),
);

CREATE TABLE Emprunter (
    date_emprunt                DATE,
    date_retour                 DATE,
    date_retour_effective       DATE,
    id_ad                       INT,
    id_ouvrage                  INT,
    FOREIGN KEY (id_ad) REFERENCES Adherent (id_ad),
    FOREIGN key (id_ouvrage) REFERENCES Ouvrage(id_ouvrage),
    CONSTRAINT max_ouvrages_empruntes CHECK (SELECT COUNT(*) FROM Emprunter WHERE id_ad = NEW.id_ad) <= 5

)

CREATE TABLE Rediger (
    id_aut              INT,
    id_ouvrage          INT,
    FOREIGN KEY (id_aut) REFERENCES Auteur (id_aut), 
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage) 
);

CREATE TABLE Referencer (
    id_ouvrage          INT,
    id_mc               INT,
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage),
    FOREIGN KEY (id_mc) REFERENCES Mot_cle (id_mc)
);


-- Données pour la table Auteur
INSERT INTO Auteur (nom_aut, prenom_aut) VALUES
    ('Diop', 'Fatoumata'),
    ('Sow', 'Ousmane'),
    ('Ndiaye', 'Mariama');

-- Données pour la table Adherent
INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES
    ('Gassama', 'Fatou', 'Pavillon Q', '778945612'),
    ('Ndao', 'Daour', 'Rufisque', '777777777'),
    ('Thiam', 'Tham', '12 Rue Dakar', '766543219');

-- Données pour la table Mot_cle
INSERT INTO Mot_cle (nom_mc) VALUES
    ('Roman'),
    ('Policier'),
    ('Science-fiction');

-- Données pour la table Rayon
INSERT INTO Rayon (nom_rayon) VALUES
    ('Fiction'),
    ('Non-fiction'),
    ('Jeunesse');

-- Données pour la table Ouvrage
INSERT INTO Ouvrage (titre, id_rayon) VALUES
    ("L'enfant noir", 1),
    ('Le Mandat', 1),
    ('Xala', 2);

-- Données pour la table Rediger
INSERT INTO Rediger (id_aut, id_ouvrage) VALUES
    (1, 1),
    (2, 2),
    (3, 3);

-- Données pour la table Referencer
INSERT INTO Referencer (id_ouvrage, id_mc) VALUES
    (1, 1),
    (2, 2),
    (3, 3);

-- Données pour la table Emprunter
INSERT INTO Emprunter (date_emprunt, date_retour, date_retour_effective, id_ad, id_ouvrage) VALUES
    ('2023-04-01', '2023-04-15', '2023-04-18', 1, 1),
    ('2023-04-05', '2023-04-20', NULL, 2, 2),
    ('2023-04-08', '2023-04-22', NULL, 3, 3);



--CAS 3

CREATE DATABASE Bibliotheque3;

use Bibliotheque2;

CREATE TABLE Auteur (
    id_aut              INT AUTO_INCREMENT PRIMARY KEY,
    nom_aut             VARCHAR(15),
    prenom_aut          VARCHAR(15)
);

CREATE TABLE Adherent (
    id_ad               INT AUTO_INCREMENT PRIMARY KEY,
    nom_ad              VARCHAR(15),
    prenom_ad           VARCHAR(15),
    adresse_ad          VARCHAR(15),
    tel_ad              INT(9)
);

CREATE TABLE Mot_cle (
    id_mc               INT AUTO_INCREMENT PRIMARY KEY,
    nom_mc              VARCHAR(15)
);

CREATE TABLE Rayon (
    id_rayon            INT AUTO_INCREMENT PRIMARY KEY,
    nom_rayon           VARCHAR(15)
);

CREATE TABLE Ouvrage (
    id_ouvrage          INT AUTO_INCREMENT PRIMARY KEY,
    titre               VARCHAR(15),
    nbr_exemp           INT,
    id_rayon            INT,
    id_aut              INT,
    FOREIGN KEY (id_rayon) REFERENCES Rayon (id_rayon),
    FOREIGN KEY (id_aut)   REFERENCES Auteur (id_aut)
);


CREATE TABLE Emprunter (
    date_emprunt                DATE,
    date_retour                 DATE,
    date_retour_effective       DATE,
    id_ad                       INT,
    id_ouvrage                   INT,
    FOREIGN KEY (id_ad) REFERENCES Adherent (id_ad),
    FOREIGN key (id_ouvrage) REFERENCES Ouvrage(id_ouvrage),
    CONSTRAINT max_ouvrages_empruntes CHECK (SELECT COUNT(*) FROM Emprunter WHERE id_ad = NEW.id_ad) <= 5

);

CREATE TABLE Rediger (
    id_aut              INT,
    id_ouvrage          INT,
    FOREIGN KEY (id_aut) REFERENCES Auteur (id_aut), 
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage) 
);

CREATE TABLE Referencer (
    id_ouvrage          INT,
    id_mc               INT,
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage),
    FOREIGN KEY (id_mc) REFERENCES Mot_cle (id_mc)
);


INSERT INTO Auteur (nom_aut, prenom_aut) VALUES
('Diallo', 'Mamadou'),
('Fall', 'Aminata'),
('Ndiaye', 'Ousmane');

INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES
('Sow', 'Fatou', 'Dakar', 778123456),
('Diop', 'Omar', 'Thies', 775987654),
('Mbaye', 'Ndeye', 'Saint-Louis', 781234567);

INSERT INTO Mot_cle (nom_mc) VALUES
('Romance'),
('Science-fiction'),
('Histoire');

INSERT INTO Rayon (nom_rayon) VALUES
('Fiction'),
('Non-fiction'),
('Jeunesse');

INSERT INTO Ouvrage (titre, nbr_exemp, id_rayon, id_aut) VALUES
('Le Soleil des indépendances', 3, 1, 3),
('L''Enfant noir', 5, 1, 2),
('Le ventre de l''Atlantique', 2, 2, 1);

INSERT INTO Emprunter (date_emprunt, date_retour, id_ad, id_ouvrage) VALUES
('2023-04-29', '2023-05-13', 1, 1),
('2023-04-29', '2023-05-13', 2, 3);

INSERT INTO Rediger (id_aut, id_ouvrage) VALUES
(1, 2),
(2, 3);

INSERT INTO Referencer (id_ouvrage, id_mc) VALUES
(1, 3),
(2, 1);






--CAS 4

CREATE DATABASE Bibliotheque4;
USE Bibliotheque4;


CREATE TABLE Auteur (
    id_aut              INT AUTO_INCREMENT PRIMARY KEY,
    nom_aut             VARCHAR(15),
    prenom_aut          VARCHAR(15)
);

CREATE TABLE Adherent (
    id_ad               INT AUTO_INCREMENT PRIMARY KEY,
    nom_ad              VARCHAR(15),
    prenom_ad           VARCHAR(15),
    adresse_ad          VARCHAR(15),
    tel_ad              INT(9)
);

CREATE TABLE Mot_cle (
    id_mc               INT AUTO_INCREMENT PRIMARY KEY,
    nom_mc              VARCHAR(15)
);

CREATE TABLE Rayon (
    id_rayon            INT AUTO_INCREMENT PRIMARY KEY,
    nom_rayon           VARCHAR(15)
);

CREATE TABLE Ouvrage (
    id_ouvrage          INT AUTO_INCREMENT PRIMARY KEY,
    titre               VARCHAR(15),
    nbr_exemp           INT,
    id_rayon            INT,
    id_aut              INT,
    FOREIGN KEY (id_aut) REFERENCES Auteur (id_aut),
    FOREIGN KEY (id_rayon) REFERENCES Rayon (id_rayon)
);


CREATE TABLE Emprunter (
    date_emprunt                DATE,
    date_retour                 DATE,
    date_retour_effective       DATE,
    id_ad                       INT,
    id_ouvrage                   INT,
    FOREIGN KEY (id_ad) REFERENCES Adherent (id_ad),
    FOREIGN key (id_ouvrage) REFERENCES Ouvrage(id_ouvrage),
    CONSTRAINT max_ouvrages_empruntes CHECK (SELECT COUNT(*) FROM Emprunter WHERE id_ad = NEW.id_ad) <= 5

);

CREATE TABLE Rediger (
    id_aut              INT,
    id_ouvrage          INT,
    FOREIGN KEY (id_aut) REFERENCES Auteur (id_aut), 
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage) 
);

CREATE TABLE Referencer (
    id_ouvrage          INT,
    id_mc               INT,
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage),
    FOREIGN KEY (id_mc) REFERENCES Mot_cle (id_mc)
);

CREATE TABLE centrale (
    id_cent             INT AUTO_INCREMENT PRIMARY key,
    nom_cent            VARCHAR(15),
    adresse             VARCHAR(20)
);


CREATE TABLE antenne (
    id_ant              INT AUTO_INCREMENT PRIMARY KEY,
    nom_ant              VARCHAR(15),
    adresse             VARCHAR(20),
    id_cent              INT,
    FOREIGN KEY (id_cent) REFERENCES centrale (id_cent)
);

CREATE TABLE contient (
    id_ouvrage           INT,
    id_ant               INT,
    FOREIGN KEY (id_ouvrage) REFERENCES Ouvrage (id_ouvrage),
    FOREIGN KEY (id_ant) REFERENCES antenne (id_ant)
);

-- Insertion d'auteurs sénégalais
INSERT INTO Auteur (nom_aut, prenom_aut) VALUES
('Sow', 'Fatou'),
('Ndiaye', 'Mamadou'),
('Thiam', 'Moussa'),
('Fall', 'Aminata'),
('Diallo', 'Ousmane');

-- Insertion d'adhérents avec des adresses et des numéros de téléphone sénégalais
INSERT INTO Adherent (nom_ad, prenom_ad, adresse_ad, tel_ad) VALUES
('Diop', 'Aminata', 'Dakar', '77 123 45 67'),
('Sylla', 'Moussa', 'Saint-Louis', '76 234 56 78'),
('Dione', 'Fatoumata', 'Kaolack', '77 345 67 89'),
('Thiaw', 'Mamadou', 'Touba', '76 456 78 90'),
('Dieng', 'Ousmane', 'Ziguinchor', '77 567 89 01');

-- Insertion de rayons
INSERT INTO Rayon (nom_rayon) VALUES
('Littérature'),
('Sciences'),
('Histoire');

-- Insertion d'ouvrages avec leurs auteurs et leur rayon correspondant
INSERT INTO Ouvrage (titre, nbr_exemp, id_rayon, id_aut) VALUES
('Un chant écarlate', 3, 1, 1),
('Le mystère de la matière noire', 2, 2, 2),
('Histoire du Sénégal', 5, 3, 3),
("Larmes d'Afrique", 1, 1, 4),
('Le génie africain', 4, 2, 5);

-- Insertion de mots-clés
INSERT INTO Mot_cle (nom_mc) VALUES
('Roman'),
('Science-fiction'),
('Histoire'),
('Afrique'),
('Sénégal');

-- Insertion des références entre ouvrages et mots-clés
INSERT INTO Referencer (id_ouvrage, id_mc) VALUES
(1, 1),
(1, 4),
(2, 2),
(3, 3),
(3, 4),
(3, 5),
(4, 1),
(4, 4),
(5, 2),
(5, 5);

-- Insertion d'une centrale et de deux antennes associées
INSERT INTO centrale (nom_cent, adresse) VALUES
('Bibliothèque centrale de Dakar', 'Boulevard STM, Dakar');

INSERT INTO antenne (nom_ant, adresse, id_cent) VALUES
('Bibliothèque de Grand-Yoff', 'Rue 10 x 17, Grand-Yoff, Dakar', 1),
('Bibliothèque de Ouakam', 'Rue 13 x 14, Ouakam, Dakar', 1);

-- Insertion d'une relation entre un ouvrage et une antenne
INSERT INTO contient (id_ouvrage, id_ant) VALUES
(1, 1);


--EXERCICE3
CREATE DATABASE aquarium;
USE aquarium;

CREATE TABLE Piece (
    id_piece INT AUTO_INCREMENT PRIMARY key,
    nom_piece VARCHAR(15)
);

CREATE TABLE bassin (
    id_bassin INT AUTO_INCREMENT PRIMARY KEY,
    nom_bassin VARCHAR(15),
    superficie INT NOT NULL,
    id_piece INT,
    FOREIGN KEY (id_piece) REFERENCES Piece(id_piece)
);

CREATE TABLE soin (
    id_soin INT AUTO_INCREMENT PRIMARY KEY,
    nature_soin VARCHAR(50)
);

CREATE TABLE ordre (
    id_ordre INT AUTO_INCREMENT PRIMARY KEY,
    nom_ordre VARCHAR(15)
);

CREATE TABLE famille (
    id_famille INT AUTO_INCREMENT PRIMARY KEY,
    nom_famille VARCHAR(15),
    id_ordre INT,
    FOREIGN KEY (id_ordre) REFERENCES ordre(id_ordre)
);

CREATE TABLE genre (
    id_genre INT AUTO_INCREMENT PRIMARY KEY,
    nom_genre VARCHAR(15),
    id_famille INT,
    FOREIGN KEY (id_famille) REFERENCES famille(id_famille)
);

CREATE TABLE espece (
    id_espece INT AUTO_INCREMENT PRIMARY KEY,
    nom_espece VARCHAR(15),
    id_genre INT,
    FOREIGN KEY (id_genre) REFERENCES genre(id_genre)
);

CREATE TABLE animal (
    id_animal INT AUTO_INCREMENT PRIMARY KEY,
    nom_animal VARCHAR(15),
    age INT,
    id_espece INT,
    FOREIGN KEY (id_espece) REFERENCES espece(id_espece),
    id_bassin INT,
    FOREIGN KEY (id_bassin) REFERENCES bassin(id_bassin)
);

CREATE TABLE soigner (
    date_soin DATE,
    id_animal INT,
    id_soin INT, 
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (id_soin) REFERENCES soin(id_soin)
);

CREATE TABLE deplacer (
    id_dep INT AUTO_INCREMENT PRIMARY KEY,
    date_dep DATE,
    id_animal INT,
    id_bassin INT,
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal),
    FOREIGN KEY (id_bassin) REFERENCES bassin(id_bassin)
);


INSERT INTO Piece(nom_piece) VALUES 
    ('Roches'),
    ('Plantes'),
    ('Sable'),
    ('Décorations');

INSERT INTO ordre(nom_ordre) VALUES 
    ('Perciformes'),
    ('Siluriformes'),
    ('Cypriniformes');

INSERT INTO famille(nom_famille, id_ordre) VALUES 
    ('Cichlidés', 1),
    ('Poeciliidés', 1),
    ('Callichthyidés', 2);

INSERT INTO genre(nom_genre, id_famille) VALUES 
    ('Poisson-ange', 1),
    ('Guppy', 2),
    ('Corydoras', 3);

INSERT INTO espece(nom_espece, id_genre) VALUES 
    ('Pterophyllum scalare', 1),
    ('Poecilia reticulata', 2),
    ('Corydoras paleatus', 3);

INSERT INTO bassin(nom_bassin, superficie, id_piece) VALUES 
    ('Bassin 1', 50, 1),
    ('Bassin 2', 80, 2),
    ('Bassin 3', 120, 3),
    ('Bassin 4', 150, 4);

INSERT INTO animal(nom_animal, age, id_espece, id_bassin) VALUES 
    ('Poisson-ange 1', 2, 1, 1),
    ('Poisson-ange 2', 3, 1, 1),
    ('Guppy 1', 1, 2, 2),
    ('Corydoras 1', 1, 3, 3);

INSERT INTO soin(nature_soin) VALUES 
    ('Traitement contre les parasites'),
    ('Changement d''eau'),
    ('Alimentation spéciale');

INSERT INTO soigner(date_soin, id_animal, id_soin) VALUES 
    ('2023-04-20', 1, 2),
    ('2023-04-25', 2, 1);

INSERT INTO deplacer(date_dep, id_animal, id_bassin) VALUES 
    ('2023-04-22', 1, 2),
    ('2023-04-26', 2, 3);
