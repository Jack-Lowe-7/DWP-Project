import sqlite3

# Connect to the database
conn = sqlite3.connect('NEF.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.executescript('''create table students (
	name TEXT,
	form TEXT,
	stamps INTEGER,
	emailPre TXT PRIMARY KEY UNIQUE,
	mainClass TEXT
);
insert into students (name, form, stamps, emailPre, mainClass) values ('Lilias Rugg', 'Newton', 201, '19lilias.r', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Muriel Vardon', 'Pasteur', 283, '19muriel.v', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Mickie Ashwin', 'Maxwell', 826, '19mickie.a', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Pasquale Dickins', 'Maxwell', 404, '19pasquale.d', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Archie Stallworth', 'Newton', 25, '19archie.s', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Cherey Garner', 'Newton', 370, '19cherey.g', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Scotti Hay', 'Newton', 725, '19scotti.h', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Michal Withers', 'Newton', 885, '19michal.w', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Anallese Pilipets', 'Maxwell', 935, '19anallese.p', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Hayden Lackmann', 'Maxwell', 194, '19hayden.l', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Rickey de Cullip', 'Pasteur', 316, '19rickey.d', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kathryn O''Keevan', 'Newton', 983, '19kathryn.o', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Lynna Banger', 'Pasteur', 341, '19lynna.b', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Antoni Di Biaggi', 'Pasteur', 163, '19antoni.d', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Leena Heal', 'Maxwell', 237, '19leena.h', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Ranna Prendergrass', 'Pasteur', 449, '19ranna.p', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Randee Humberstone', 'Pasteur', 40, '19randee.h', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Howey Eye', 'Newton', 202, '19howey.e', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Lebbie Hulls', 'Maxwell', 777, '19lebbie.h', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Keelby Newbatt', 'Maxwell', 277, '19keelby.n', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Sarajane Hull', 'Maxwell', 32, '19sarajane.h', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Arabela Ales', 'Pasteur', 427, '19arabela.a', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Alyce MacNab', 'Maxwell', 823, '19alyce.m', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Annadiana Ever', 'Pasteur', 451, '19annadiana.e', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Margy Kitteman', 'Pasteur', 657, '19margy.k', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Harv Heeps', 'Pasteur', 194, '19harv.h', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Morena Cadogan', 'Newton', 773, '19morena.c', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Addia McGuire', 'Maxwell', 769, '19addia.m', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Flynn Brodeau', 'Pasteur', 346, '19flynn.b', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Odelia Lannen', 'Pasteur', 722, '19odelia.l', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Giacobo Rothwell', 'Maxwell', 71, '19giacobo.r', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Denny Castaner', 'Newton', 571, '19denny.c', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Francine Gladyer', 'Maxwell', 179, '19francine.g', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Sibley Chafer', 'Maxwell', 637, '19sibley.c', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Ezmeralda Kiessel', 'Maxwell', 929, '19ezmeralda.k', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Barbra Jeromson', 'Maxwell', 161, '19barbra.j', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Yancey Wykey', 'Pasteur', 213, '19yancey.w', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Marquita Uccello', 'Newton', 100, '19marquita.u', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Lianna McGregor', 'Pasteur', 354, '19lianna.m', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Cobbie Hatton', 'Pasteur', 709, '19cobbie.h', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Peg Hort', 'Newton', 547, '19peg.h', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Juditha Aps', 'Maxwell', 973, '19juditha.a', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Adelbert Ashworth', 'Pasteur', 73, '19adelbert.a', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Sharon Paridge', 'Maxwell', 603, '19sharon.p', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Bale McCarrell', 'Pasteur', 679, '19bale.m', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Killy Scain', 'Maxwell', 496, '19killy.s', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Guss Arnout', 'Maxwell', 136, '19guss.a', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Tobiah Basilio', 'Maxwell', 18, '19tobiah.b', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Julienne Pascho', 'Newton', 915, '19julienne.p', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Linn Schonfelder', 'Newton', 137, '19linn.s', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Neila Plaid', 'Newton', 25, '19neila.p', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Joane Sigward', 'Newton', 100, '19joane.s', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Madeleine Penner', 'Pasteur', 238, '19madeleine.p', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Vlad Lafflina', 'Newton', 204, '19vlad.l', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Nelle Kumar', 'Newton', 900, '19nelle.k', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Cherey Blackledge', 'Pasteur', 108, '19cherey.b', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Arney Lasslett', 'Pasteur', 43, '19arney.l', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Karole Titchmarsh', 'Maxwell', 295, '19karole.t', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Ignaz Baxill', 'Newton', 513, '19ignaz.b', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Dave Meddemmen', 'Newton', 339, '19dave.m', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kiah Yegorev', 'Newton', 741, '19kiah.y', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Clevey Dalyell', 'Pasteur', 772, '19clevey.d', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Dolph Mickelwright', 'Maxwell', 63, '19dolph.m', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Gregoire Cherrison', 'Newton', 840, '19gregoire.c', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Wilton Urion', 'Maxwell', 719, '19wilton.u', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Martin O''Neil', 'Newton', 924, '19martin.o', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Randi Napoli', 'Newton', 871, '19randi.n', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Rudyard Dunphy', 'Newton', 689, '19rudyard.d', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Norah Wavell', 'Newton', 188, '19norah.w', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kelby Abeau', 'Pasteur', 760, '19kelby.a', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Husein Matt', 'Maxwell', 428, '19husein.m', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Augustus Bowyer', 'Pasteur', 18, '19augustus.b', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Washington Barbey', 'Pasteur', 443, '19washington.b', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kelli Croyden', 'Newton', 400, '19kelli.c', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Esme Delap', 'Newton', 874, '19esme.d', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Lesya Buntain', 'Maxwell', 985, '19lesya.b', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Patrizia Twinterman', 'Maxwell', 853, '19patrizia.t', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Margie MacTrustey', 'Newton', 470, '19margie.m', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Meghann Melpuss', 'Pasteur', 736, '19meghann.m', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Vern Gemlbett', 'Maxwell', 701, '19vern.g', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Iseabal Snoddon', 'Newton', 114, '19iseabal.s', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Moll Simioni', 'Newton', 417, '19moll.s', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Donnamarie Fennessy', 'Maxwell', 961, '19donnamarie.f', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Saw Bailes', 'Maxwell', 206, '19saw.b', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Boycie Giocannoni', 'Maxwell', 356, '19boycie.g', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Stanton Rangall', 'Maxwell', 500, '19stanton.r', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Laurella Edlin', 'Maxwell', 201, '19laurella.e', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Thorny Chinnery', 'Pasteur', 315, '19thorny.c', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Thayne Arnley', 'Newton', 325, '19thayne.a', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kirk Lepper', 'Newton', 768, '19kirk.l', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Grover Mazey', 'Maxwell', 846, '19grover.m', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Emelia Anyene', 'Newton', 279, '19emelia.a', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Tansy Reyne', 'Newton', 195, '19tansy.r', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Kandace Carlaw', 'Pasteur', 83, '19kandace.c', 'Swan');
insert into students (name, form, stamps, emailPre, mainClass) values ('Maurise Sawkin', 'Pasteur', 697, '19maurise.s', 'Halley');
insert into students (name, form, stamps, emailPre, mainClass) values ('Arden Pedrollo', 'Newton', 913, '19arden.p', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Nomi Evins', 'Pasteur', 688, '19nomi.e', 'Curie');
insert into students (name, form, stamps, emailPre, mainClass) values ('Cly Raggitt', 'Maxwell', 408, '19cly.r', 'Pascal');
insert into students (name, form, stamps, emailPre, mainClass) values ('Verna Sabati', 'Newton', 931, '19verna.s', 'Watt');
insert into students (name, form, stamps, emailPre, mainClass) values ('Lemuel Bentzen', 'Maxwell', 681, '19lemuel.b', 'Curie');''')




# Close the connection
conn.close()
