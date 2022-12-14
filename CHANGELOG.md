# Changelog

## [1.5.0](https://github.com/googleapis/python-service-usage/compare/v1.4.3...v1.5.0) (2022-12-14)


### Features

* Add support for `google.cloud.service_usage.__version__` ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* Add typing to proto.Message based class attributes ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))


### Bug Fixes

* Add dict typing for client_options ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))
* Drop usage of pkg_resources ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))
* Fix timeout default values ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([c13d3f6](https://github.com/googleapis/python-service-usage/commit/c13d3f63188f5171e4af1f13757f3b89ee92f408))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([a2eb0d7](https://github.com/googleapis/python-service-usage/commit/a2eb0d7ff9ae9db36c3d0c0ac8c67284c0581ea9))

## [1.4.3](https://github.com/googleapis/python-service-usage/compare/v1.4.2...v1.4.3) (2022-10-07)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#148](https://github.com/googleapis/python-service-usage/issues/148)) ([b8cc381](https://github.com/googleapis/python-service-usage/commit/b8cc38152251900cb6c75b91585a465eb1b0de66))

## [1.4.2](https://github.com/googleapis/python-service-usage/compare/v1.4.1...v1.4.2) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#146](https://github.com/googleapis/python-service-usage/issues/146)) ([99d8d9e](https://github.com/googleapis/python-service-usage/commit/99d8d9e4282f5ab5c930055a0ac7ddfa6d399f44))

## [1.4.1](https://github.com/googleapis/python-service-usage/compare/v1.4.0...v1.4.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#133](https://github.com/googleapis/python-service-usage/issues/133)) ([586a7f9](https://github.com/googleapis/python-service-usage/commit/586a7f92c6658c907cd990461a9a9beb45f7514a))
* **deps:** require proto-plus >= 1.22.0 ([586a7f9](https://github.com/googleapis/python-service-usage/commit/586a7f92c6658c907cd990461a9a9beb45f7514a))

## [1.4.0](https://github.com/googleapis/python-service-usage/compare/v1.3.2...v1.4.0) (2022-07-16)


### Features

* add audience parameter ([c0745b9](https://github.com/googleapis/python-service-usage/commit/c0745b92bae9a8f5dd8e2c2bf992984de422eb46))


### Bug Fixes

* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([#127](https://github.com/googleapis/python-service-usage/issues/127)) ([90975b7](https://github.com/googleapis/python-service-usage/commit/90975b7f86a1dcbbd7029e7860aee750a2cc243c))
* require python 3.7+ ([#125](https://github.com/googleapis/python-service-usage/issues/125)) ([c9de01e](https://github.com/googleapis/python-service-usage/commit/c9de01e72298c164fefb9243ab96bb3020484ab3))

## [1.3.2](https://github.com/googleapis/python-service-usage/compare/v1.3.1...v1.3.2) (2022-06-03)


### Bug Fixes

* **deps:** require protobuf <4.0.0dev ([#115](https://github.com/googleapis/python-service-usage/issues/115)) ([fc546f2](https://github.com/googleapis/python-service-usage/commit/fc546f2dc727e8b358d62f4f9958006c04b35c4c))


### Documentation

* fix changelog header to consistent size ([#116](https://github.com/googleapis/python-service-usage/issues/116)) ([1c9df92](https://github.com/googleapis/python-service-usage/commit/1c9df92b379f9735477bd7c7d590a9280e944fbd))

## [1.3.1](https://github.com/googleapis/python-service-usage/compare/v1.3.0...v1.3.1) (2022-03-05)


### Bug Fixes

* **deps:** require google-api-core>=1.31.5, >=2.3.2 ([#88](https://github.com/googleapis/python-service-usage/issues/88)) ([bee9ae0](https://github.com/googleapis/python-service-usage/commit/bee9ae00c8dd77fcc423ceb4b0023b0041d6c395))

## [1.3.0](https://github.com/googleapis/python-service-usage/compare/v1.2.1...v1.3.0) (2022-02-26)


### Features

* add api key support ([#74](https://github.com/googleapis/python-service-usage/issues/74)) ([c9cf774](https://github.com/googleapis/python-service-usage/commit/c9cf774ba8082ce7026acd582817e84b63d39fbe))


### Bug Fixes

* resolve DuplicateCredentialArgs error when using credentials_file ([27fb0c2](https://github.com/googleapis/python-service-usage/commit/27fb0c270dc776862f282159c9a637aa5900ced7))


### Documentation

* add generated snippets ([#79](https://github.com/googleapis/python-service-usage/issues/79)) ([dee08f1](https://github.com/googleapis/python-service-usage/commit/dee08f1d654cb5e04955ca51c824f77b13c000b9))

## [1.2.1](https://www.github.com/googleapis/python-service-usage/compare/v1.2.0...v1.2.1) (2021-11-01)


### Bug Fixes

* **deps:** drop packaging dependency ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))
* **deps:** require google-api-core >= 1.28.0 ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))


### Documentation

* list oneofs in docstring ([57a982c](https://www.github.com/googleapis/python-service-usage/commit/57a982c7cafb2f91a9c2d2f0f8b85be1502f14be))

## [1.2.0](https://www.github.com/googleapis/python-service-usage/compare/v1.1.0...v1.2.0) (2021-10-18)


### Features

* add support for python 3.10 ([#53](https://www.github.com/googleapis/python-service-usage/issues/53)) ([9f235a8](https://www.github.com/googleapis/python-service-usage/commit/9f235a84d01b84a598f5af4bdd6203f4d752f31a))

## [1.1.0](https://www.github.com/googleapis/python-service-usage/compare/v1.0.1...v1.1.0) (2021-10-07)


### Features

* add context manager support in client ([#49](https://www.github.com/googleapis/python-service-usage/issues/49)) ([b50e7cb](https://www.github.com/googleapis/python-service-usage/commit/b50e7cbbf53e0efb6809bce5c25cdc7369e65f5d))


### Bug Fixes

* improper types in pagers generation ([b230f5f](https://www.github.com/googleapis/python-service-usage/commit/b230f5fd83f21b7ac86bb01dac85ce403d694228))

## [1.0.1](https://www.github.com/googleapis/python-service-usage/compare/v1.0.0...v1.0.1) (2021-09-24)


### Bug Fixes

* add 'dict' annotation type to 'request' ([172ba0d](https://www.github.com/googleapis/python-service-usage/commit/172ba0dd5ca2d1d6ffee0cccce45ee28c822704b))

## [1.0.0](https://www.github.com/googleapis/python-service-usage/compare/v0.2.2...v1.0.0) (2021-08-03)


### Features

* bump release level to production/stable ([#28](https://www.github.com/googleapis/python-service-usage/issues/28)) ([6627d2d](https://www.github.com/googleapis/python-service-usage/commit/6627d2dddf686a6ecc355891989928ca33003f00))

## [0.2.2](https://www.github.com/googleapis/python-service-usage/compare/v0.2.1...v0.2.2) (2021-07-29)


### Bug Fixes

* enable self signed jwt for grpc ([#24](https://www.github.com/googleapis/python-service-usage/issues/24)) ([cb9bed0](https://www.github.com/googleapis/python-service-usage/commit/cb9bed079e5ab4316ae79d44c8cf4bee1b4c3ae7))


### Documentation

* add Samples section to CONTRIBUTING.rst ([#20](https://www.github.com/googleapis/python-service-usage/issues/20)) ([394ed1a](https://www.github.com/googleapis/python-service-usage/commit/394ed1a75dcfa2c70f8bbac6aaea1150a6d90052))


### Miscellaneous Chores

* release as 0.2.2 ([#25](https://www.github.com/googleapis/python-service-usage/issues/25)) ([4f1ab38](https://www.github.com/googleapis/python-service-usage/commit/4f1ab3848cf43ae7385ebf5c4dcb5f1b9057f14d))

## [0.2.1](https://www.github.com/googleapis/python-service-usage/compare/v0.2.0...v0.2.1) (2021-07-21)


### Bug Fixes

* **deps:** pin 'google-{api,cloud}-core', 'google-auth' to allow 2.x versions ([#19](https://www.github.com/googleapis/python-service-usage/issues/19)) ([599eee0](https://www.github.com/googleapis/python-service-usage/commit/599eee0fe0f92efa4a19835691a9216c8804349f))

## [0.2.0](https://www.github.com/googleapis/python-service-usage/compare/v0.1.0...v0.2.0) (2021-07-14)


### Features

* add always_use_jwt_access ([#10](https://www.github.com/googleapis/python-service-usage/issues/10)) ([87d2c40](https://www.github.com/googleapis/python-service-usage/commit/87d2c40eb4989b94229984f22e461fdc56a4f122))


### Bug Fixes

* disable always_use_jwt_access ([#14](https://www.github.com/googleapis/python-service-usage/issues/14)) ([2f90720](https://www.github.com/googleapis/python-service-usage/commit/2f907209d1199c5a9cec210495845775ae630ccf))


### Documentation

* omit mention of Python 2.7 in 'CONTRIBUTING.rst' ([#1127](https://www.github.com/googleapis/python-service-usage/issues/1127)) ([#5](https://www.github.com/googleapis/python-service-usage/issues/5)) ([c8bbbcb](https://www.github.com/googleapis/python-service-usage/commit/c8bbbcbd939b421fa0b243f6003de54afc2107e1))

## 0.1.0 (2021-06-14)


### Features

* generate v1 ([b468d1b](https://www.github.com/googleapis/python-service-usage/commit/b468d1b447c30994d9266b5e0ff4c34ec0d19d80))
