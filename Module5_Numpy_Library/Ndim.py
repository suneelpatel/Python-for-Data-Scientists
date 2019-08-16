# import pandas as pd
# import numpy as np
#
# df=pd.Series(np.arange(1,51))
# print(df.ndim)
#
# import pandas as pd
# import numpy as np
#
# df=pd.Series(np.arange(1,51))
# print(df.axes)
#
# # import pandas as pd
# # import numpy as np
# #
# # df=pd.Series(np.arange(1,51))
# # print(df.values)
# #
# import pandas as pd
# import numpy as np
#
# df=pd.Series(np.arange(1,51))
# print(df.head(6))
#
#
# import pandas as pd
# import numpy as np
#
# df=pd.Series(np.arange(1,51))
# print(df.tail(6))
#
import pandas as pd
import numpy as np

d=pd.DataFrame({'odd':np.arange(1, 100, 2),
   'even':np.arange(0, 100, 2)})
print(d['odd'])
print(d['even'])
df=pd.DataFrame(d)
print(df.sum())

#
# import pandas as pd
# import numpy as np
#
# d={'odd':np.arange(1,100,2),
#    'even':np.arange(0,100,2)}
# print(d['odd'])
# print(d['even'])
# df=pd.DataFrame(d)
# print(df.sum())

#
# import pandas as pd
# import numpy as np
#
# d={'odd':np.arange(1,100,2),
#    'even':np.arange(0,100,2)}
# print(d['odd'])
# print(d['even'])
# df=pd.DataFrame(d)
# print(df.std())
