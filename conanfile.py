from conans import ConanFile, tools
import os

required_conan_version = ">=1.33.0"


class MpmcqueueConan(ConanFile):
    name = "mpmcqueue"
    description = "A bounded multi-producer multi-consumer concurrent queue written in C++11."
    license = "MIT"
    topics = ("mpmcqueue", "queue", "concurrency")
    homepage = "https://github.com/rigtorp/MPMCQueue"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, 11)

    def package_id(self):
        self.info.header_only()

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination=self._source_subfolder, strip_root=True)

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "MPMCQueue"
        self.cpp_info.names["cmake_find_package_multi"] = "MPMCQueue"
