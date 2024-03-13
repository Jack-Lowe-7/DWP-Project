import sqlite3

# Connect to the database
conn = sqlite3.connect('NEF.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.executescript("""create table students (
	name VARCHAR(50),
	form VARCHAR(7),
	stamps INT,
	emailpre VARCHAR(50),
	mainclass VARCHAR(6),
	password VARCHAR(50)
);
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Elyssa Lamborne', 'Maxwell', 281, '19lamborne.e', 'Swan', 'lE2!g#XiJm<');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Nadeen Housden', 'Newton', 125, '19housden.n', 'Halley', 'yI3,T0B0O2C');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Melina Creyke', 'Maxwell', 945, '19creyke.m', 'Swan', 'vC3>T$a+2(Fr');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Loretta Hakeworth', 'Maxwell', 136, '19hakeworth.l', 'Halley', 'vV8&w!+@');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Jake Beetham', 'Maxwell', 317, '19beetham.j', 'Swan', 'mV2X6w|vBg');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Robinet Solomonides', 'Maxwell', 341, '19solomonides.r', 'Swan', 'bO2(_NtTXuZ!');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Claudette Prewer', 'Pasteur', 64, '19prewer.c', 'Pascal', 'oX8`)AlWb');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Gualterio Andell', 'Newton', 177, '19andell.g', 'Halley', 'dY7&iT&+BfS');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Elli Grigorkin', 'Maxwell', 445, '19grigorkin.e', 'Watt', 'rY5,@GQ=p}Ynrm');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Filmer Pedrocchi', 'Newton', 841, '19pedrocchi.f', 'Curie', 'aR8>1z~P&q');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Celestina Dagger', 'Pasteur', 205, '19dagger.c', 'Swan', 'uX1VX#}CR|');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Cassandre Reignolds', 'Newton', 663, '19reignolds.c', 'Watt', 'rH1<|$o<Em+VEQ6,');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Gae Dionisetti', 'Newton', 382, '19dionisetti.g', 'Pascal', 'sW0.k7E%q<');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Norris Remnant', 'Maxwell', 959, '19remnant.n', 'Watt', 'kY9B+)xBuG|(R,');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Ardelle Dymock', 'Pasteur', 866, '19dymock.a', 'Halley', 'lM2(xjc&#JS');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Yoshi Cassels', 'Pasteur', 277, '19cassels.y', 'Swan', 'vY8{G1h.');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Reynolds Dursley', 'Newton', 128, '19dursley.r', 'Pascal', 'gK0,|(.3~s5wY');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Berkley Dally', 'Newton', 595, '19dally.b', 'Halley', 'pE6&#J#RX');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Biddie Steptowe', 'Pasteur', 435, '19steptowe.b', 'Curie', 'dA4<W>t58!$r');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Sammie Delahunty', 'Maxwell', 105, '19delahunty.s', 'Pascal', 'nF0|$O,t');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Adam Long', 'Newton', 578, '19long.a', 'Swan', 'kL8<!E0v');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Muffin Van Der Weedenburg', 'Maxwell', 176, '19van.m', 'Watt', 'hP9pKl<X');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Grata Clayhill', 'Newton', 479, '19clayhill.g', 'Pascal', 'kA6~CRzDPkIQM');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Alaine Bartlett', 'Maxwell', 392, '19bartlett.a', 'Swan', 'tL0~p6K!WC');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Rasla Cotte', 'Newton', 709, '19cotte.r', 'Halley', 'nV4BIwq');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Bernardine Moughtin', 'Pasteur', 509, '19moughtin.b', 'Watt', 'iB3{s<eD');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Brigida Faltin', 'Newton', 938, '19faltin.b', 'Pascal', 'cM3bF)O}t?8');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Wells Lie', 'Maxwell', 966, '19lie.w', 'Pascal', 'zI5>bN%4');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Starlene Imlach', 'Newton', 355, '19imlach.s', 'Watt', 'vK3#t4cCnM3F');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Rafaello Prott', 'Pasteur', 810, '19prott.r', 'Curie', 'zW1~{BU');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Janot Stanistrete', 'Maxwell', 143, '19stanistrete.j', 'Pascal', 'lZ6#8zRj');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Elenore Coolahan', 'Newton', 394, '19coolahan.e', 'Pascal', 'lX3)F1?1Rz');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Karlie Zanuciolii', 'Maxwell', 901, '19zanuciolii.k', 'Swan', 'bL9.?nO');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Berta Jirieck', 'Newton', 540, '19jirieck.b', 'Swan', 'aI7!i+tCLvY<Z0');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Hyman Doumenc', 'Pasteur', 489, '19doumenc.h', 'Halley', 'kP1=x5dTdj&A?');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Poul Renahan', 'Newton', 319, '19renahan.p', 'Watt', 'uC0{eq&aZ|L0R1@=');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Isahella Drysdell', 'Pasteur', 428, '19drysdell.i', 'Watt', 'rA4`WHNaFAE');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Marlyn Borkett', 'Pasteur', 503, '19borkett.m', 'Pascal', 'oB4|lbHv5bB@?');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Kelcy Gollop', 'Newton', 915, '19gollop.k', 'Pascal', 'hH6J9P2C$f|!=');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Dalila Bamford', 'Maxwell', 8, '19bamford.d', 'Swan', 'zB2@uSnQi');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Guthrie Lanchester', 'Pasteur', 412, '19lanchester.g', 'Watt', 'yT6!GE3sF{ppq0');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Lennie Minshull', 'Maxwell', 57, '19minshull.l', 'Curie', 'lE8+P4BxJ3rcw?');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Melania Gookey', 'Newton', 467, '19gookey.m', 'Swan', 'bA8}iFfWXur4BA$');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Kerby Lawless', 'Maxwell', 335, '19lawless.k', 'Halley', 'sC5<n56cF~94O@');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Ruperta Lau', 'Maxwell', 656, '19lau.r', 'Pascal', 'aT3~IL');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Doralynne Hoggan', 'Maxwell', 69, '19hoggan.d', 'Watt', 'wB2{!W7xD');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Faber Docket', 'Pasteur', 224, '19docket.f', 'Swan', 'qG9F(&_A4');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Kissie Casford', 'Maxwell', 941, '19casford.k', 'Pascal', 'hL8|z.sh7U!7');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Griswold Le Clercq', 'Maxwell', 154, '19le.g', 'Curie', 'sF9(7OAG');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Cacilie Salzen', 'Maxwell', 194, '19salzen.c', 'Pascal', 'oN8+t&4ziAJuU');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Nicolina Slocum', 'Newton', 741, '19slocum.n', 'Curie', 'dH8<?LdcO%z)');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Kiley Kaesmakers', 'Maxwell', 700, '19kaesmakers.k', 'Pascal', 'uM2|.|xHTvpMnT.');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Henryetta Westwood', 'Maxwell', 973, '19westwood.h', 'Watt', 'pC6@,P1QA0?<x');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Jenine Barlee', 'Newton', 65, '19barlee.j', 'Halley', 'mZ5!M}AV6~=');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Gage Birchner', 'Newton', 63, '19birchner.g', 'Swan', 'tR0|hPPhrwyR');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Georgette Trewartha', 'Pasteur', 672, '19trewartha.g', 'Curie', 'hQ2#YZAR');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Cam Crosetti', 'Pasteur', 846, '19crosetti.c', 'Pascal', 'rL2.r@6YV)9pF!6');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Ketty Frenzel;', 'Maxwell', 196, '19frenzel;.k', 'Watt', 'lH9KEpe#y`DoWK6');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Hillary Lomen', 'Pasteur', 727, '19lomen.h', 'Watt', 'sZ1>NhY0AktTbD');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Asher MacFarland', 'Pasteur', 528, '19macfarland.a', 'Pascal', 'kU2!6{zzZ7');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Jeff Hopfer', 'Maxwell', 756, '19hopfer.j', 'Watt', 'cM6#2MuSM=Ho7');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Hank Probyn', 'Pasteur', 897, '19probyn.h', 'Pascal', 'mY7=x5dpkvxx|');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Foss Ortas', 'Newton', 742, '19ortas.f', 'Swan', 'bZ49UiQ~y');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Alfi Budgen', 'Maxwell', 542, '19budgen.a', 'Halley', 'kC5)~hQ)c?z7EXy');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Lory Kitteman', 'Pasteur', 910, '19kitteman.l', 'Swan', 'hK7}zD}pNqGMb');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Dido Fourman', 'Newton', 485, '19fourman.d', 'Watt', 'rC1!kn)y');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Elora Hebbard', 'Maxwell', 396, '19hebbard.e', 'Pascal', 'sH5+.lHV4');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Bunnie Eallis', 'Maxwell', 616, '19eallis.b', 'Watt', 'mR8@`DQoYg');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Hermione Charrier', 'Newton', 590, '19charrier.h', 'Swan', 'aS3`#.&>r&&c');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Tannie Tebbe', 'Newton', 625, '19tebbe.t', 'Watt', 'iT1_$=lZe?');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Gun Nibloe', 'Pasteur', 441, '19nibloe.g', 'Pascal', 'wS5!#B}8');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Eward Karlsson', 'Pasteur', 135, '19karlsson.e', 'Halley', 'aM6%<(l');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Zsazsa Nystrom', 'Newton', 692, '19nystrom.z', 'Swan', 'bX1%YbnI+m');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Clyve Bonny', 'Newton', 183, '19bonny.c', 'Watt', 'wE2,9{YC');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Sapphire Langstrath', 'Newton', 528, '19langstrath.s', 'Watt', 'kR3|85}aby?Uy');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Mariette Torrance', 'Maxwell', 977, '19torrance.m', 'Watt', 'kM6!Wb?p=)');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Chastity Balasin', 'Maxwell', 613, '19balasin.c', 'Halley', 'dJ3|ZT%h7LgP');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Clive Klus', 'Maxwell', 489, '19klus.c', 'Curie', 'fQ52g`U');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Addy Ruoff', 'Maxwell', 695, '19ruoff.a', 'Swan', 'qK4.no.4+?4}');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Jessamyn Nealey', 'Pasteur', 894, '19nealey.j', 'Curie', 'iX95_{vPD,');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Bidget Kaemena', 'Maxwell', 434, '19kaemena.b', 'Pascal', 'rD6=KPvIt7');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Meridith Toderi', 'Maxwell', 745, '19toderi.m', 'Watt', 'lU2$)vez~OI#');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Halette Stowe', 'Newton', 511, '19stowe.h', 'Halley', 'qZ6(5G6=aQVM2');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Packston O''Halleghane', 'Pasteur', 214, '19o''halleghane.p', 'Halley', 'bM6)&xa_3FJ@uu');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Emmalynn Dugdale', 'Pasteur', 64, '19dugdale.e', 'Halley', 'hQ9<iYX2BtS>(z');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Joell Aglione', 'Newton', 12, '19aglione.j', 'Watt', 'pN0+YqMQ');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Noel Swyer-Sexey', 'Pasteur', 146, '19swyer-sexey.n', 'Watt', 'hX2>.M5{%');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Charline Allenby', 'Maxwell', 913, '19allenby.c', 'Halley', 'xU0=XW1cNC_4');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Merilee Morgue', 'Pasteur', 449, '19morgue.m', 'Swan', 'oW2xG1V=2WG3G');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Carolann Huyge', 'Maxwell', 65, '19huyge.c', 'Halley', 'qQ9!H{.Y');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Bobette Tunno', 'Maxwell', 87, '19tunno.b', 'Watt', 'hS9).&9K|y');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Ellene Ruthven', 'Maxwell', 14, '19ruthven.e', 'Curie', 'hS8)(U2yws9K');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Abagael Cheesman', 'Pasteur', 359, '19cheesman.a', 'Watt', 'dV2?~#O');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Tudor Westley', 'Newton', 224, '19westley.t', 'Pascal', 'fJ4_<,gyR4oiC');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Dannie Gentric', 'Maxwell', 196, '19gentric.d', 'Watt', 'nX0<zQ,,`_Fv@}h');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Hart Treversh', 'Maxwell', 327, '19treversh.h', 'Pascal', 'uM9|Jhcm}&n3Y');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Brittni Hans', 'Newton', 36, '19hans.b', 'Curie', 'zB1|jKpgJLAdk?Zj');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Kamillah Capini', 'Maxwell', 517, '19capini.k', 'Curie', 'bU6#.cbP');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Merci Renvoys', 'Pasteur', 52, '19renvoys.m', 'Watt', 'zB8@@TFW$');
insert into students (name, form, stamps, emailpre, mainclass, password) values ('Norris Burbage', 'Maxwell', 224, '19burbage.n', 'Swan', 'oD8=alEAxM4');
                create table staff (
	name VARCHAR(50),
	form VARCHAR(7),
	emailpre VARCHAR(50),
	password VARCHAR(50)
);
insert into staff (name, form, emailpre, password) values ('Nelia Arnold', 'Maxwell', 'nelia.arnold', 'qD3{IzGA>,');
insert into staff (name, form, emailpre, password) values ('Gasper Trood', 'Maxwell', 'gasper.trood', 'pS3@?)djSH2?');
insert into staff (name, form, emailpre, password) values ('Haily Elsmere', 'Newton', 'haily.elsmere', 'aX8(tA{3~8&M');
insert into staff (name, form, emailpre, password) values ('Felike Chester', 'Newton', 'felike.chester', 'qY3)3zpeDYm~0=O');
insert into staff (name, form, emailpre, password) values ('Elihu Edgars', 'Newton', 'elihu.edgars', 'wJ2<<t+D$');
insert into staff (name, form, emailpre, password) values ('Tome Gun', 'Newton', 'tome.gun', 'gN4,joGD{$CQn}r');
insert into staff (name, form, emailpre, password) values ('Ricoriki Matchett', 'Maxwell', 'ricoriki.matchett', 'jM3`w)_wAbne`');
insert into staff (name, form, emailpre, password) values ('Rycca Gyngyll', 'Maxwell', 'rycca.gyngyll', 'iO8!!q+9jx3CH|E0');
insert into staff (name, form, emailpre, password) values ('Gilles Luciani', 'Maxwell', 'gilles.luciani', 'bQ8JDXrZ');
insert into staff (name, form, emailpre, password) values ('Deerdre Swadling', 'Maxwell', 'deerdre.swadling', 'qN2~yN3ePb(4');
insert into staff (name, form, emailpre, password) values ('Joseito Bynert', 'Newton', 'joseito.bynert', 'tN8>5DI4@0J');
insert into staff (name, form, emailpre, password) values ('Frans Biasetti', 'Pasteur', 'frans.biasetti', 'uF6>Hja&cplBEv)');
insert into staff (name, form, emailpre, password) values ('Charin Whordley', 'Maxwell', 'charin.whordley', 'mB9!CJUwsY');
insert into staff (name, form, emailpre, password) values ('Donetta Lummus', 'Pasteur', 'donetta.lummus', 'jS5%1|d%5');
insert into staff (name, form, emailpre, password) values ('Merci Althrope', 'Maxwell', 'merci.althrope', 'gO7{BqA$W36rO+v');
insert into staff (name, form, emailpre, password) values ('Johnny Whenham', 'Pasteur', 'johnny.whenham', 'vT5(P8c_ml');
insert into staff (name, form, emailpre, password) values ('Sindee Abramovicz', 'Maxwell', 'sindee.abramovicz', 'rW0cI&b');
insert into staff (name, form, emailpre, password) values ('Debbie Salterne', 'Newton', 'debbie.salterne', 'vT5f{vAae)RUy');""")



# Close the connection
conn.close()
