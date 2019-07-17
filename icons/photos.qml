<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.8.0-Zanzibar" simplifyDrawingHints="0" simplifyDrawingTol="1" simplifyMaxScale="1" styleCategories="AllStyleCategories" readOnly="0" labelsEnabled="0" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" simplifyAlgorithm="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 type="singleSymbol" symbollevels="0" enableorderby="0" forceraster="0">
    <symbols>
      <symbol type="marker" force_rhr="0" alpha="1" clip_to_extent="1" name="0">
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0.00000000000000006,-10"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5.4"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="size">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="if( &quot;AZIMUTH&quot; !=0,5.4,0)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="97,97,97,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="14"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="false" name="active"/>
                  <Option type="QString" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="-2,1"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="false" name="active"/>
                  <Option type="QString" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="triangle"/>
          <prop k="offset" v="2,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="7"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="false" name="active"/>
                  <Option type="QString" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
        <layer class="SimpleMarker" pass="0" locked="0" enabled="1">
          <prop k="angle" v="0"/>
          <prop k="color" v="97,97,97,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="square"/>
          <prop k="offset" v="-1,-3"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="Pixel"/>
          <prop k="outline_color" v="0,0,0,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="Pixel"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="Pixel"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="false" name="active"/>
                  <Option type="QString" value="if(TO_REAL( &quot;Azimuth&quot; )=0,'',TO_REAL( &quot;Azimuth&quot; ))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
                <Option type="Map" name="size">
                  <Option type="bool" value="false" name="active"/>
                  <Option type="QString" value="if( &quot;AZIMUTH&quot; !=0,2,0)" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="ID" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory scaleBasedVisibility="0" backgroundColor="#ffffff" height="15" maxScaleDenominator="1e+08" lineSizeType="MM" lineSizeScale="3x:0,0,0,0,0,0" enabled="0" scaleDependency="Area" diagramOrientation="Up" labelPlacementMethod="XHeight" sizeType="MM" width="15" minScaleDenominator="0" barWidth="5" backgroundAlpha="255" opacity="1" minimumSize="0" penAlpha="255" penColor="#000000" sizeScale="3x:0,0,0,0,0,0" penWidth="0" rotationOffset="270">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" priority="0" zIndex="0" obstacle="0" showAll="1" placement="0" dist="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="ID">
      <editWidget type="Hidden">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Date">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Time">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lon">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Lat">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Altitude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="North">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Azimuth">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Mak">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Camera Mod">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Title">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Comment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Path">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="RelPath">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Timestamp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="ID" name="" index="0"/>
    <alias field="Name" name="" index="1"/>
    <alias field="Date" name="" index="2"/>
    <alias field="Time" name="" index="3"/>
    <alias field="Lon" name="" index="4"/>
    <alias field="Lat" name="" index="5"/>
    <alias field="Altitude" name="" index="6"/>
    <alias field="North" name="" index="7"/>
    <alias field="Azimuth" name="" index="8"/>
    <alias field="Camera Mak" name="" index="9"/>
    <alias field="Camera Mod" name="" index="10"/>
    <alias field="Title" name="" index="11"/>
    <alias field="Comment" name="" index="12"/>
    <alias field="Path" name="" index="13"/>
    <alias field="RelPath" name="" index="14"/>
    <alias field="Timestamp" name="" index="15"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="ID" applyOnUpdate="0" expression=""/>
    <default field="Name" applyOnUpdate="0" expression=""/>
    <default field="Date" applyOnUpdate="0" expression=""/>
    <default field="Time" applyOnUpdate="0" expression=""/>
    <default field="Lon" applyOnUpdate="0" expression=""/>
    <default field="Lat" applyOnUpdate="0" expression=""/>
    <default field="Altitude" applyOnUpdate="0" expression=""/>
    <default field="North" applyOnUpdate="0" expression=""/>
    <default field="Azimuth" applyOnUpdate="0" expression=""/>
    <default field="Camera Mak" applyOnUpdate="0" expression=""/>
    <default field="Camera Mod" applyOnUpdate="0" expression=""/>
    <default field="Title" applyOnUpdate="0" expression=""/>
    <default field="Comment" applyOnUpdate="0" expression=""/>
    <default field="Path" applyOnUpdate="0" expression=""/>
    <default field="RelPath" applyOnUpdate="0" expression=""/>
    <default field="Timestamp" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="ID" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Name" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Date" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Time" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Lon" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Lat" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Altitude" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="North" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Azimuth" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Camera Mak" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Camera Mod" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Title" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Comment" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Path" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="RelPath" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
    <constraint field="Timestamp" notnull_strength="0" unique_strength="0" exp_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="ID" desc="" exp=""/>
    <constraint field="Name" desc="" exp=""/>
    <constraint field="Date" desc="" exp=""/>
    <constraint field="Time" desc="" exp=""/>
    <constraint field="Lon" desc="" exp=""/>
    <constraint field="Lat" desc="" exp=""/>
    <constraint field="Altitude" desc="" exp=""/>
    <constraint field="North" desc="" exp=""/>
    <constraint field="Azimuth" desc="" exp=""/>
    <constraint field="Camera Mak" desc="" exp=""/>
    <constraint field="Camera Mod" desc="" exp=""/>
    <constraint field="Title" desc="" exp=""/>
    <constraint field="Comment" desc="" exp=""/>
    <constraint field="Path" desc="" exp=""/>
    <constraint field="RelPath" desc="" exp=""/>
    <constraint field="Timestamp" desc="" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" actionWidgetStyle="dropDown" sortExpression="&quot;Camera Model&quot;">
    <columns>
      <column type="field" name="ID" width="-1" hidden="0"/>
      <column type="actions" width="-1" hidden="1"/>
      <column type="field" name="Name" width="-1" hidden="0"/>
      <column type="field" name="Date" width="-1" hidden="0"/>
      <column type="field" name="Time" width="-1" hidden="0"/>
      <column type="field" name="Lon" width="-1" hidden="0"/>
      <column type="field" name="Lat" width="-1" hidden="0"/>
      <column type="field" name="Altitude" width="-1" hidden="0"/>
      <column type="field" name="North" width="-1" hidden="0"/>
      <column type="field" name="Azimuth" width="-1" hidden="0"/>
      <column type="field" name="Path" width="-1" hidden="0"/>
      <column type="field" name="Camera Mak" width="-1" hidden="0"/>
      <column type="field" name="Camera Mod" width="-1" hidden="0"/>
      <column type="field" name="Title" width="-1" hidden="0"/>
      <column type="field" name="Comment" width="-1" hidden="0"/>
      <column type="field" name="RelPath" width="-1" hidden="0"/>
      <column type="field" name="Timestamp" width="-1" hidden="0"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="ALTITUDE" editable="1"/>
    <field name="AZIMUTH" editable="1"/>
    <field name="Altitude" editable="1"/>
    <field name="Azimuth" editable="1"/>
    <field name="CAMERA MAK" editable="1"/>
    <field name="CAMERA MOD" editable="1"/>
    <field name="Camera Mak" editable="1"/>
    <field name="Camera Maker" editable="1"/>
    <field name="Camera Mod" editable="1"/>
    <field name="Camera Model" editable="1"/>
    <field name="Comment" editable="1"/>
    <field name="DATE" editable="1"/>
    <field name="Date" editable="1"/>
    <field name="ID" editable="1"/>
    <field name="LAT" editable="1"/>
    <field name="LON" editable="1"/>
    <field name="Lat" editable="1"/>
    <field name="Lon" editable="1"/>
    <field name="NAME" editable="1"/>
    <field name="NORTH" editable="1"/>
    <field name="Name" editable="1"/>
    <field name="North" editable="1"/>
    <field name="PATH" editable="1"/>
    <field name="Path" editable="1"/>
    <field name="RelPath" editable="1"/>
    <field name="TIME" editable="1"/>
    <field name="Time" editable="1"/>
    <field name="Timestamp" editable="1"/>
    <field name="Title" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="ALTITUDE"/>
    <field labelOnTop="0" name="AZIMUTH"/>
    <field labelOnTop="0" name="Altitude"/>
    <field labelOnTop="0" name="Azimuth"/>
    <field labelOnTop="0" name="CAMERA MAK"/>
    <field labelOnTop="0" name="CAMERA MOD"/>
    <field labelOnTop="0" name="Camera Mak"/>
    <field labelOnTop="0" name="Camera Maker"/>
    <field labelOnTop="0" name="Camera Mod"/>
    <field labelOnTop="0" name="Camera Model"/>
    <field labelOnTop="0" name="Comment"/>
    <field labelOnTop="0" name="DATE"/>
    <field labelOnTop="0" name="Date"/>
    <field labelOnTop="0" name="ID"/>
    <field labelOnTop="0" name="LAT"/>
    <field labelOnTop="0" name="LON"/>
    <field labelOnTop="0" name="Lat"/>
    <field labelOnTop="0" name="Lon"/>
    <field labelOnTop="0" name="NAME"/>
    <field labelOnTop="0" name="NORTH"/>
    <field labelOnTop="0" name="Name"/>
    <field labelOnTop="0" name="North"/>
    <field labelOnTop="0" name="PATH"/>
    <field labelOnTop="0" name="Path"/>
    <field labelOnTop="0" name="RelPath"/>
    <field labelOnTop="0" name="TIME"/>
    <field labelOnTop="0" name="Time"/>
    <field labelOnTop="0" name="Timestamp"/>
    <field labelOnTop="0" name="Title"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>Name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
