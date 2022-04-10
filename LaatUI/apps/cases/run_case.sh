cd $(cd $(dirname $0);pwd)
cd ..
cd ..
cd Cy
#yarn cypress run --no-exit --reporter=spec &> $(cd $(dirname $0);pwd)/logs
#yarn cypress run --reporter=junit &> /Users/sunxinyang/Desktop/LaatUI/LaatUI/apps/cases/logs
#yarn cypress run --reporter junit --reporter-options "mochaFile=results/test_output.xml,toConsole=true"
docker run -v /LaatUI/LaatUI/Cy:/e2e -w /e2e cypress/included:3.2.0 &> $(cd $(dirname $0);pwd)/logs