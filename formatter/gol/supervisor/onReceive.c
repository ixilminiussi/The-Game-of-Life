#include <definitions.h>
//@@//

if (!SUPSTATE(failed))
{
    if (MSG(gen) == GRAPHPROPERTIES(end))
    {
        SUPSTATE(finishedCells)
        ++;

        fprintf(SUPSTATE(resultFile), "%d,%d,%d,%d\n", MSG(x), MSG(y), MSG(gen), MSG(alive));

        if (SUPSTATE(finishedCells) >= GRAPHPROPERTIES(cellCount))
        {
            Super::stop_application();
        }
    }
}