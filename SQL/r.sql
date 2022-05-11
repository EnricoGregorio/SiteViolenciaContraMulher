USE dbcamara;

SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Violência psicológica (ameaça)';
SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Lesão corporal';
SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Perseguição';
SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Injúria';
SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Feminicídio';
SELECT COUNT(p.idnatufato) FROM VitimasAgressores AS p INNER JOIN NaturezasFato As n ON n.id = p.idnatufato WHERE n.natureza = 'Outra';