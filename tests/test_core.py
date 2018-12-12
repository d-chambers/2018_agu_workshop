"""
Tests for berktempy
"""

from berktempy.core import download_data


aust_data = download_data('australia')


# In[27]:


assert isinstance(aust_data, str)
assert len(aust_data)





# tests for str output


# tests for generating a file
import tempfile
tf = tempfile.NamedTemporaryFile(mode='w')
tf_path = Path(tf.name)
_ = download_data('turkey', path=tf_path)


# In[36]:


assert tf_path.exists()
assert tf_path.stat().st_size > 0


# Load the data using numpy (skip the header records which are marked with a `%`).

# In[77]:
out = load_data(aust_data)
assert isinstance(out, np.ndarray)
assert len(out)

