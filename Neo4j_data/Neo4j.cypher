LOAD CSV FROM 'file:///teams.csv' AS line
CREATE (:Team { team_name: line[0]})

LOAD CSV FROM 'file:///states.csv' AS line
CREATE (:State { state_name: line[0]})

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///neo4jdata.csv" AS row
  MATCH (p:State {state_name: row.state}), (t:Team {team_name: row.team})
  CREATE (p)-[:Edge {cnt: row.cnt, avg: row.avg, povern: row.povern}]->(t)

MATCH p=()-[r:Edge]->() Where toInt(r.cnt)>1000 and toFloat(r.avg)>0.3 return p;